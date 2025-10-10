---
title: RAG Integration
slug: /integracao-rag
---

---

# 📚 Sprint 14 – RAG Integration and Initial Testing

## 🎯 Objective

Integrate a fully functional Retrieval-Augmented Generation (RAG) pipeline, with the goal of validating end-to-end functionality.

Flow:
- Upload a public notice (PDF)
- Preprocessing and indexing of the document
- Natural-language question answering via a language model (LLM)
- Contextual responses informed by relevant document excerpts
- Initial conversational pipeline testing

## ✅ Deliverables

- ✅ Functional MVP of the complete RAG pipeline running locally
- ✅ First working front-end (CLI-based interface)
- ✅ Sample Q&A results based on the uploaded edital
- ✅ Logs listing source documents for all answers
- ✅ Initial output precision observation (compared to human validation)

---

## 🧠 Technical Overview of the Pipeline

### 🗃️ Input: PDF Document

We use LangChain’s PyPDFLoader to load and convert the official notice into structured document objects.

```python
loader = PyPDFLoader("data/edital.pdf")
documents = loader.load()
```

### 🔎 Text Splitting

To ensure effective retrieval while maintaining context, the text is chunked into 1000-character blocks with a 100-character overlap.

```python
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)
```

### 📐 Embeddings + Vector Store

OpenAI's embedding model is used to transform textual chunks into semantic vectors. These vectors are stored with FAISS for efficient similarity search.

```python
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
```

### 🤖 LLM + RAG Pipeline

We used the GPT-3.5 Turbo model to build a question-answering chain by combining generative capability with retrieval of contextual vectors from FAISS.

```python
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)
```

### 💬 Sample Query

Query:
> "What are the technical requirements for participating in this notice?"

Example Output:
```txt
🔍 Question: What are the technical requirements for participating in this notice?

📌 Answer: [Generated response from the model]

📄 Source documents:
- edital.pdf (page 2)
- edital.pdf (page 3)
```

---

## 🧪 Tests & Evaluation

Tested questions:

1. "What are the financial requirements of this notice?"
2. "Can ATOS participate using certificates X and Y?"

Observations:

| Item | Evaluation Metric                    | Status       |
|------|--------------------------------------|--------------|
| 1    | Model comprehension                  | ✅ Acceptable |
| 2    | Answer accuracy                      | ⚠️ Partially correct |
| 3    | Source tracking for transparency     | ✅ Working    |
| 4    | Clarity and relevance of answers     | ✅ Clear & Objective |

---

## 🔍 Known Limitations

- The model struggles slightly with negative conditions, exceptions, or highly detailed legal criteria.
- The front-end is currently a CLI — not yet user-friendly for broader testing.
- FAISS index is rebuilt every execution; not persisted.
- Lacks structured logging and storage for queries/responses.

---

## 🚀 Next Steps (Sprint 15)

- Develop a more intuitive front-end (notebook, Streamlit, or Gradio UI)
- Add FAISS persistence to disk (avoid re-indexing)
- Improve accuracy evaluation (e.g., human vs model via F1-score)
- Add proper text normalization and regex sanitization

---

## 📦 Project Structure

```
project/
│
├── data/
│   └── edital.pdf
│
├── src/
│   └── main.py  ← Full RAG pipeline
│
├── .env          ← API keys stored here
└── requirements.txt
```

---

## 🧩 Tech Stack

- 🧠 OpenAI GPT (GPT-3.5 Turbo)
- 🧱 LangChain
- 🗂️ FAISS vector DB
- 📄 PyPDFLoader
- 🔐 dotenv (.env for secure config)

---