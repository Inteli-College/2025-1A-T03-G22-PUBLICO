---
title: Sprint 12
slug: /sprint-12
---

##  Data Retrieval Strategy Definition
###  1: Review of the Data to Be Retrieved
**Goal:** Thoroughly understand the types of information the system needs to extract from public notices (editais) in order to accurately answer user queries or build project requirements.
- **Examples of data to retrieve**:
  - Technical requirements (e.g., expertise in a specific technology, required certifications).
  - Financial requirements (e.g., minimum revenue, contractual guarantees).
  - Deadlines for delivery and execution.
  - Eligibility and evaluation criteria.
  - Terms such as “mandatory requirements”, “participation conditions”.
📌 **Practical task:** Read through 1 or 2 public notices and manually annotate where this information appears, how it is written, and whether there are patterns that can help structure the indexing.

---
###  2: Choosing a Data Retrieval Approach
**Goal:** Select the most appropriate data retrieval approach: simple text search, vector embeddings, or a hybrid solution.
- **Possible approaches**:
  - ✅ **Semantic search with embeddings** (recommended for RAG): transforms document snippets into vectors for similarity comparison with user queries.
  - ❎ **Keyword-based search** (e.g., TF-IDF): simpler but less effective with synonyms or the complex language of public notices.
  - 🧠 **Hybrid search**: combines keyword search with contextual embeddings.
📌 **Practical task:** Deep dive into tools such as:
  - **FAISS** or **Chroma** (fast vector storage)
  - **Embedding transformers** like `all-MiniLM-L6-v2` (via SentenceTransformers)
  - Consider combining OCR + NLP if the documents are scanned PDFs.

---
###  3: Definition of the Indexed Data Structure
**Goal:** Decide on the chunking strategy – how to split documents to enable effective semantic search.
- **Decisions to make**:
  - Chunk size (e.g., 500–1000 tokens)
  - Overlap between chunks (e.g., 200 tokens)
  - Section detection (e.g., “OBJETO”, “DAS CONDIÇÕES”)
📌 **Practical task:**
  - Prototype a script using `PyMuPDF` or `pdfplumber` to extract and split a public notice.
  - Experiment with different chunk sizes and overlaps.

---
###  4: Initial Prototype of the Vector Database
**Goal:** Create and populate a vector database with public notice chunks.
- Recommended tools:
  - `Chroma`
  - `FAISS`
  - `Weaviate` or `Pinecone`
📌 **Practical task**:
  - Use a real public notice.
  - Parse it into clean text.
  - Generate embeddings with `SentenceTransformers`.
  - Store the vectorized chunks in FAISS.
  - Run a simple query and check which excerpts are retrieved.

---
###  5: Technical Decision Documentation
**Goal:** Record the decisions made during this sprint.
📌 Must include:
- Why vector/hybrid search was chosen
- Which embedding model was used
- How documents are being chunked
- Which vector database was used
- Example of created indexes + screenshots of tests
- Estimated document volume (how many chunks per public notice?)
```