import pdfplumber
from typing import List
from sentence_transformers import SentenceTransformer, CrossEncoder
import faiss
import numpy as np
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize

# ===========================================================
# 1. EXTRAÇÃO DO TEXTO DO PDF
# ===========================================================
def extract_text_from_pdf(file_path: str) -> str:
    full_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n\n"
    return full_text


# ===========================================================
# 2. CHUNKING DO TEXTO (Seções/Parágrafos)
# ===========================================================
def chunk_by_sections(text: str, max_words: int = 300) -> List[str]:
    sections = text.split("\n\n")
    chunks = []
    current_chunk = []
    current_len = 0

    for sec in sections:
        words = sec.split()
        if current_len + len(words) > max_words:
            chunks.append(" ".join(current_chunk))
            current_chunk, current_len = [], 0
        current_chunk.extend(words)
        current_len += len(words)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


# ===========================================================
# 3. CRIAÇÃO DA BASE FAISS
# ===========================================================
def criar_base_vetorial(chunks: List[str]):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks, show_progress_bar=True)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    faiss.write_index(index, "index_edital.faiss")
    print("✅ Índice FAISS criado e salvo.")
    return model, index, embeddings


# ===========================================================
# 4. FILTRO POR PALAVRAS-CHAVE
# ===========================================================
def keyword_filter(candidates: List[str], query: str, keywords: List[str] = None) -> List[str]:
    """
    Caso seja fornecida uma lista de palavras-chave, dá prioridade a chunks que contenham
    essas palavras antes de passar ao rerank.
    """
    if not keywords:
        return candidates

    filtered = []
    for chunk in candidates:
        for kw in keywords:
            if kw.lower() in chunk.lower():
                filtered.append(chunk)
                break  # evita adicionar o mesmo chunk várias vezes

    # Se nenhum chunk passar no filtro, retorna todos (fallback)
    return filtered if filtered else candidates


# ===========================================================
# 5. CONSULTA COM FILTRO + RERANK
# ===========================================================
def consulta_simples(index, model, chunks: List[str], k: int = 15):
    query = input("\nDigite uma pergunta: ")

    # Embedding da query
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=k)
    candidates = [chunks[idx] for idx in I[0]]

    # 🔍 Detecta palavras relevantes da query automaticamente
    # ex: "critério de julgamento" => ["critério", "julgamento"]
    keywords = [w for w in query.lower().split() if len(w) > 5]

    # Filtra candidatos que contenham palavras-chave
    candidates = keyword_filter(candidates, query, keywords)

    # 🔥 Rerank
    reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    scores = reranker.predict([(query, doc) for doc in candidates])

    results = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)

    print("\n🔎 Resultados mais relevantes (com pré-filtro + rerank):")
    for i, (chunk, score) in enumerate(results[:3]):
        print(f"\n--- Resultado {i+1} (score={score:.4f}) ---")
        print(chunk[:600])  # mostra só os primeiros caracteres


# ===========================================================
# 6. EXECUÇÃO DO PIPELINE
# ===========================================================
if __name__ == "__main__":
    file_path = "edital_exemplo.pdf"  # seu edital aqui

    print("\n📂 Extraindo texto do PDF...")
    texto = extract_text_from_pdf(file_path)

    print("\n🪓 Realizando chunking...")
    chunks = chunk_by_sections(texto)
    print(f"🧩 {len(chunks)} chunks gerados.")

    print("\n🔧 Criando índice vetorial...")
    model, index, embeddings = criar_base_vetorial(chunks)

    print("\n❓ Pronto para perguntas!")
    consulta_simples(index, model, chunks)