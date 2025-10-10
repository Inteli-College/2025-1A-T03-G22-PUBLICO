---
title: Final Testing
slug: /final-testing
---


## 📚 **Sprint 15 — Final Testing and System Reliability Validation**

### 🎯 **Objective**
The main goal of this sprint was to validate the **stability, accuracy, and reliability** of the Retrieval-Augmented Generation (RAG) system developed throughout the previous sprints.

Functional, performance, and consistency tests were conducted to ensure that:
- The system maintained coherence in responses under different queries;  
- The sources returned were traceable and correct;  
- The average response time was adequate for real-world usage;  
- No crashes, freezes, or loss of context occurred during multiple interactions.  

---

### 🧪 **Test Strategy**
During this sprint, testing was divided into four main groups:

#### 1. **Functional Tests (End-to-End)**
> Verification of the complete pipeline execution: loading → indexing → querying → answer generation.

- **Input:** Official PDF (`edital_SP_2024.pdf`)  
- **Validation:** The system correctly answered real questions and returned the appropriate sources.  
- **Result:** ✅ All steps executed successfully.  

#### 2. **Reliability/Consistency Tests**
> Verification of response coherence for similar and repeated questions.  

- **Question 1A:** “What are the technical requirements of the notice?”  
- **Question 1B:** “What is required to prove technical capability?”  

**Expected result:** Semantically equivalent answers, with the same cited sources.  
**Result obtained:** ✅ Consistency maintained (minimal linguistic variation).  

#### 3. **Performance Tests**
> Evaluation of processing and retrieval time.

| Scenario | Metric | Result | Status |
|-----------|---------|---------|---------|
| Indexing 1 PDF (22 pages) | Total time | 12 s | ✅ |
| Simple query | Average response time | 2.8 s | ✅ |
| Multiple queries (two consecutive questions) | Average response time | 5.1 s | ⚠️ (slight expected increase) |

#### 4. **Robustness Tests**
> Analysis of system behavior under unusual or erroneous inputs.

| Test Case | Example Input | Expected Result | Obtained Result |
|------------|----------------|------------------|-----------------|
| Irrelevant question | “Who won the 2010 World Cup?” | Standard message: “Out of scope” | ✅ Returned: “This information is not present in the document.” |
| Empty PDF | File with no text | Error handled gracefully (no crash) | ✅ OK |
| PDF with tables | Notice including tabular annexes | Partial reading, no crash | ⚠️ Partial reading, as expected |

---

### 📊 **Examples of Executed Tests**

**Question 1:**  
> “What are the financial requirements of this notice?”  
**Answer obtained:**  
The notice requires proof of financial capacity through net equity and balance sheets from the last two fiscal years.  
**Sources:**  
`edital_SP_2024.pdf`, pages 14–15  
**Validation:** Consistent with the original document. ✅  

**Question 2:**  
> “Is there any contractual guarantee required?”  
**Answer obtained:**  
Yes. The notice requires a contractual guarantee of 5% of the total value, in compliance with applicable legislation.  
**Sources:**  
`edital_SP_2024.pdf`, page 28  
**Validation:** Text consistent and page reference correct. ✅  

---

### ⚙️ **Test Infrastructure**
- **Environment:** Local (Notebook + Python v3.10)  
- **Models:** `gpt-3.5-turbo` (LLM), `text-embedding-3-small` (OpenAI embeddings)  
- **Tools:** LangChain, FAISS, PyTest, Rich (for console logging)  
- **Log File:** `logs/test_results_sprint15.log`  

---

### 🔍 **Results Analysis**

| Criterion | Outcome | Observations |
|------------|----------|--------------|
| Response accuracy | High | Only minor linguistic variations |
| Source traceability | 100% correctly displayed |  |
| Overall performance | Good (< 3s per query) | Could be optimized for larger PDFs |
| Robustness (error handling) | Adequate | No crashes reported |

---

### 🚀 **Sprint Conclusion**
The RAG system is **functional, stable, and reliable** for internal use and shows full alignment with the scope defined in previous sprints.  
Final validations indicate that the retrieval and generation pipeline is ready for integration with more user-friendly interfaces (e.g., Streamlit, Gradio) or web APIs.  

✅ **Acceptance Criteria Met:**
- [x] Functional semantic retrieval  
- [x] Contextual generation without noticeable hallucination  
- [x] Visible and traceable sources  
- [x] Basic performance test approved  
- [x] Error handling implemented  

---

### 🧾 **Next Steps (Post-Sprint 15)**
1. Deploy the RAG system in a web testing environment (e.g., Streamlit UI).  
2. Automate logs and reliability reports (e.g., dashboard for answered queries).  
3. Evaluate automatic metrics for response quality (e.g., F1-score, Recall@k).  
4. Begin testing with multiple documents in the same vector database.  
