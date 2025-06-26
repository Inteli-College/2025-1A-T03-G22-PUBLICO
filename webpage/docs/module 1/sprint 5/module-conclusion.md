---
title: Module Conclusion
sidebar_position: 4
slug: /module-conclusion
---

This project focuses on the development of an innovative solution for the extraction and analysis of requirements from technical and financial documents. This module aimed to carry out a detailed requirements survey for the system, perform comparative tests with advanced models, and investigate the implementation of a vector database, enabling the use of RAG (Retrieval-Augmented Generation) techniques. The main objective is to ensure high precision in the identification of requirements, combined with an intuitive interface that allows for dynamic visualization and data exportation, thereby facilitating the decision-making process. In this way, the project stands as a robust and scalable solution, aligned with the strategic demands of the company. Below is a detailed account of the key points developed during the module:

---

### 1. Requirements Survey

- **Functional Requirements (FRs):**  
  - Essential functionalities were identified, such as document processing and summarization, interactive presentation of results with export options, and the automatic matching of certifications with bid requirements.
  - Additionally, additional (desirable) requirements were established, which include archiving usage history and implementing an analytical dashboard for data monitoring.

- **Non-Functional Requirements (NFRs):**  
  - Performance specifications were defined, such as processing time and the ability to handle documents of up to 10 MB.
  - The need for scalability to process multiple documents simultaneously was emphasized.
  - Security and usability measures were adopted to ensure the quality of the solution.

- **Prioritization:**  
  - The requirements were categorized as “mandatory” and “desirable,” allowing for strategic planning that meets the client's objectives.

---

### 2. Tests with GPT-Mini 4.0

- **Test Objective:**  
  - To evaluate the model's ability to extract and summarize the technical and financial requirements from simulated bidding documents.

- **Methodology:**  
  - Utilization of descriptive texts from AWS infrastructure projects, covering critical points such as authentication, security, API integration, and usage-based cost models.
  - Use of specific prompts to extract information about functional and non-functional requirements, identify typographical errors, and count the numbers present in the text.

- **Results Obtained:**  
  - The model demonstrated competence in extracting the key requirements, accurately identifying inconsistencies, errors, and performing the correct count of numbers.
  - The solution’s feasibility was confirmed, with the model properly configured to interpret the requirements in a structured manner.

---

### 3. Benchmark and Model Comparison

- **Tested Models:**  
  - **GPT-4.0 Mini:**  
    - Showed high performance, with high precision in extracting the requirements and following the instructions, being able to identify the five items of functional and non-functional requirements, as well as detect errors and count numbers correctly.
  - **DeepSeek V3 0324:**  
    - Encountered difficulties in fully identifying implicit criteria, such as correcting typographical errors and counting numbers, not reaching the precision demonstrated by GPT-4.0 Mini.

- **Benchmark Conclusions:**  
  - The tests revealed that GPT-4.0 Mini delivered superior results in terms of adherence to instructions and effectiveness in requirement extraction.
  - The experience reinforced the need to integrate a vector database to enhance the accuracy of the results through the use of RAG techniques.

---

### 4. Next Steps

- **Development of the Web Interface:**  
  - Build an intuitive and responsive interface, enabling clear and interactive visualization of the extracted data, with functionalities for data export and analysis.

- **Integration with a Vector Database:**  
  - Adopt a vector database that enables the implementation of RAG techniques, increasing the accuracy and relevance of the results.

- **Continuous Improvements:**  
  - Conduct ongoing analyses of the system's performance and the extraction models, using user feedback and test results to drive continuous adjustments and improvements.

- **Expansion of Test Scenarios:**  
  - Expand the database with different types of documents and contexts, validating the model’s robustness in diverse scenarios and ensuring the solution’s scalability.

---

### 5. Conclusion

The points presented demonstrate the continuous effort in structuring a robust project that combines effective requirements extraction with an interface that facilitates decision-making. Each developed step contributes to the consolidation of the solution, ensuring greater precision, usability, and scalability to meet the business's strategic demands. After the tests were performed, it was confirmed that the integration of a RAG (Retrieval-Augmented Generation) model is fundamental to guarantee the precise extraction and analysis of requirements from technical and financial documents. The combination of the vector database with the model’s ability to interpret and organize information will allow for the accurate identification of both functional and non-functional requirements, as well as the correction of inconsistencies and the detection of implicit details within the text.