from dotenv import load_dotenv
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

# === Carregar variáveis do .env ===
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("A variável OPENAI_API_KEY não está definida no .env")

# === Carregamento de documentos ===
loader = PyPDFLoader("data/edital.pdf")
documents = loader.load()

# === Divisão em chunks ===
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# === Criação de embeddings e FAISS ===
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# === Modelo LLM ===
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# === Pipeline RAG ===
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)

# === Teste ===
query = "Quais são os requisitos técnicos para a participação neste edital?"
result = qa_chain(query)

print("🔍 Pergunta:", query)
print("📌 Resposta:", result["result"])
print("📄 Fontes:")
for doc in result["source_documents"]:
    print("-", doc.metadata.get("source", ""), f"(página {doc.metadata.get('page', '?')})")