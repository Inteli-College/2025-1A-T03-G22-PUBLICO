---
title: Sprint Conclusion
slug: /indexing-structure
---

## 📦 3 – Definition of Indexed Data Structure
### 🎯 Objective
Define how documents (public notices and RFPs) will be split into smaller parts (chunks), aiming to facilitate contextual information retrieval using the RAG (Retrieval-Augmented Generation) architecture. This step enhances system performance by efficiently feeding the LLM with relevant excerpts.
---
### 🔍 Strategic Decisions
| Parameter | Definition | Justification |
|-----------|------------|----------------|
| Chunk size | 500 tokens | Balances context depth with embedding performance |
| Overlap | 100 tokens | Ensures continuity between chunks, avoiding context loss or ambiguity |
| Section detection | Typical keywords like OBJETO (PURPOSE), DAS CONDIÇÕES (TERMS), HABILITAÇÃO (QUALIFICATIONS), PRAZO (DEADLINE), etc. | Helps to quickly identify semantically or legally relevant parts of the notice |
---
### 🛠️ Practical Task: Prototyping Script
A small Python script was developed using **pdfplumber** to extract text from a public notice and structurally split it into overlapped chunks.

#### 🍃 Libraries used:
```python
import pdfplumber
import re
from typing import List
```
```