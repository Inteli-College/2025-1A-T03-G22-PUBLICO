---
title: Data Retrieval Approach
slug: /data-retrieval
---

## 🧠 2 – Data Retrieval Strategy Definition
### 🎯 Objective
Define the data retrieval strategy to be adopted in the system based on LLMs (Large Language Models), focusing on public notices and long documents such as RFPs. This step is essential to ensure that the model receives relevant information in a precise and efficient manner through an RAG (Retrieval-Augmented Generation) architecture.
---
### 🔍 Evaluated Approaches
| Approach | Description | Advantages | Disadvantages |
|----------|-------------|------------|----------------|
| 📝 **Keyword search (TF-IDF)** | Uses term frequency to rank excerpts | Simple, fast, lightweight in terms of computation | Not effective with technical language, ignores synonyms and context |
| 🧠 **Semantic search with embeddings** ✅ *Chosen* | Converts text chunks into numerical vectors to assess meaning-based similarity | Captures synonyms, context, and actual intent of the language | Requires more processing power and additional steps |
| 🔁 **Hybrid search** | Combines TF-IDF and embeddings | Balances objective precision with semantic context | More complex to implement initially |
---
### ✅ Chosen Approach: Semantic Search with Embeddings
The approach based on **vector embeddings** proved to be the most suitable for our project scenario, which deals with lengthy, formal documents with dense language — such as public procurement notices and RFPs.

For example, the public notice **SP001/2024 (EMBASA)** contains fragmented information spread over many pages, such as financial requirements, balance sheet submission criteria, and legal qualification rules, among others [1]. Manually locating this information is inefficient, and semantic search allows the system to retrieve it by meaning, even if exact terms are not used.
---
### ⚙️ Tools Used in the Prototype
| Step | Tool / Technology |
|------|--------------------|
| PDF reading | `pdfplumber` |
| Text chunking | Custom Script (500 tokens + 100 overlap) |
| Embedding generation | `SentenceTransformers` with the `all-MiniLM-L6-v2` model |
| Vector storage | `FAISS` |
| OCR for scanned PDFs (if needed) | `pytesseract` + `pdf2image` |
---
### 🧪 Practical Test
A real public notice was loaded, preprocessed, and its text divided into vectorized chunks. The following query was performed on the semantic index:

**Query:**  
> *What are the financial requirements of this public notice?*

**Result:**  
The system correctly returned excerpts such as:
- “The company must present the balance sheet for the last fiscal year.”
- “Minimum required net worth, depending on the lot value.”
- “Proof of available financial liquidity (DFL)...”
- “Companies undergoing judicial recovery must prove economic-financial capability...” [1].
---
### 🏁 Conclusion
Semantic search based on embeddings has proven to be more effective for the project's purpose, enabling content understanding even when language varies across documents. This approach was successfully validated with a real example and will be adopted as the architectural standard for the following stages:
- Integration with LLM via LangChain;
- Automatic response generation from retrieved excerpts;
- Precision and reliability evaluation of the RAG strategy.
---
### 📎 Reference
[1] Public Notice SP001/2024 – EMBASA. Available via: SEI System / LICITAÇÕES-E. Queried excerpts: qualification requirements, accounting obligations, and procurement subject.
```