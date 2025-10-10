---
title: Pipeline Rag develop
slug: /pipeline-rag
---
**Sprint 13 — Desenvolvimento do Pipeline RAG**
---

# 📑 Test Documentation — Sprint 13  

## 🎯 Test Objectives  
The tests carried out in this sprint aimed to validate the **Retrieval-Augmented Generation (RAG) pipeline** developed. Specifically, the following questions were addressed:  

1. Is the system able to load PDF documents and split them into suitable chunks for embedding creation?  
2. Does the vectorstore (FAISS) correctly retrieve the most relevant sections of the tender?  
3. Does the LLM respond to contextualized questions based only on the content of the provided document?  
4. Are the sources used displayed in the output, ensuring traceability of the answers?  

---

## 🧪 Test Strategy  
An incremental approach was adopted, starting with the verification of each component separately and then validating the entire pipeline.  

### Steps:  
1. **Document loading test:**  
   - Tender PDF documents were loaded using `PyPDFLoader`.  
   - Validation: number of pages > 0, legible text format.  
   - Result: OK.  

2. **Chunking test (text splitting):**  
   - Configuration: `chunk_size=1000`, `chunk_overlap=100`.  
   - Validation: ensured that the text was not truncated and that the overlap actually contained repeated parts for context.  
   - Result: OK, coherent chunks.  

3. **Embedding generation test:**  
   - Model: `text-embedding-3-small` (OpenAI).  
   - Validation: each chunk returned a vector with 1,536 dimensions.  
   - Result: OK, all documents indexed.  

4. **Retrieval test (Retriever):**  
   - Validation question: _“What are the technical requirements for participating in this tender?”_  
   - Expected: retrieval of excerpts mentioning technical eligibility criteria.  
   - Result: system returned 2–3 relevant excerpts, as expected.  

5. **Full RAG pipeline test (Retrieval + LLM):**  
   - Real question:  
     - Input: _“What are the technical requirements for participating in this tender?”_  
     - Output: The model returned a synthesis of excerpts mentioning the need to prove technical capacity, infrastructure, and prior project experience.  
     - Sources: pages 12 and 13 of the PDF were cited.  
   - Validation: the answer did not invent nonexistent requirements (no perceptible hallucination).  

6. **Traceability test (displaying sources):**  
   - Validation: checked whether page and file metadata were displayed along with the answers.  
   - Result: displayed correctly.  

---

## 📊 Examples of Executed Tests  

**Question 1:**  
```
What are the technical requirements for participating in this tender?
```  

**Answer obtained:**  
```
The tender requires proof of experience in providing technological infrastructure
and the submission of certificates of execution of similar services. It is also required
that the company has a qualified technical team available.
```  

**Sources:**  
```
- data/edital.pdf (page 12)
- data/edital.pdf (page 13)
```  

---

**Question 2:**  
```
Does the tender mention financial guarantees required?
```  

**Answer obtained:**  
```
Yes. The tender requires a contractual guarantee of 5% of the total value,
according to the public procurement legislation, which can be provided as surety bonds,
cash collateral, or public securities.
```  

**Sources:**  
```
- data/edital.pdf (page 47)
```  

---

## ✅ Conclusions  
- The RAG pipeline is **functional** and responds based on the content of the provided tenders.  
- Displaying the sources ensures reliability and reduces the risk of hallucinations.  
- Small adjustments to `chunk_size` and `k` (number of retrieved excerpts) can further optimize responses.  
- For upcoming sprints (14 and 15), it is recommended to:  
  - Assess scalability with multiple documents.  
  - Conduct performance tests (average response time).  
  - Investigate automatic evaluation metrics (e.g., Rouge, BLEU, Recall based on human annotations).  

---