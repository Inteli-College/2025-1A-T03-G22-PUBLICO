---
title: GPT-Mini 4.0 Test
sidebar_position: 2
slug: /gpt-mini-test
---

---

### **Tests Conducted During the Sprint**  

During this sprint, the primary focus was on implementing and evaluating a **Large Language Model (LLM)**, specifically the Chat-GPT Mini, for extracting and summarizing technical and financial requirements from a simulated public tender document. The goal of this simulated project is to develop a **cloud-based solution** leveraging **AWS infrastructure** for processing and analyzing public tenders, with an emphasis on automated requirement extraction.  

Below is the text used as the basis for testing:  

> _"The cloud project aims to implement a scalable and secure platform for processing and analyzing public tenders, utilizing an LLM (Large Language Model) to extract and summarize technical and financial requirements. The solution will be hosted on an AWS-based infrastructure, leveraging services such as S3 for document storage, Lambda for serverless processing, and DynamoDB for metadata persistence. The system will feature an intuitive web interface developed with Streamlit, allowing users to upload files in various formats (PDF, DOCX, TXT) and receive a structured summary of the key requirements of the tender. Among the functional requirements, the need for a text extraction and analysis mechanism using NLP stands out, along with a database for storing query histories and past analyses. The system must support multiple users with authentication via OAuth 2.0 and permission control for different access levels. Non-functional requirements include high availability, data security with encryption in transit and at rest, and optimized response times for large-scale queries. The architecture should be designed to handle peak loads, using Auto Scaling to ensure elasticity and a load balancer to distribute requests. In financial terms, the project must adopt a consumption-based cost model (pay-as-you-go), optimizing resource utilization to minimize operational expenses. The initial budget considers using EC2 spot instances to reduce computing costs and integrating managed services to prevent operational overhead. The solution also includes a contingency plan with automated backup and disaster recovery via AWS Backup. The financial feasibility of the project will be periodically assessed to ensure that the ROI (Return on Investment) aligns with the company's expectations and that the solution can scale sustainably as demand increases."_

---


## **Tests Conducted**  

To validate the implementation of the LLM, a test was performed where the fictitious project text was submitted to the model, along with a prompt specifying the aspects to be extracted and summarized. The prompt used was:  

> _"Identify and summarize the technical and financial requirements for participation in the project described above. List the key elements related to infrastructure, authentication criteria, security, and financial evaluation, as well as any mandatory participation requirements."_

### **Evaluation Results**  

The model generated the following response:  

> **### Technical Requirements**  
>  
> 1. **Infrastructure:**  
>    - **Platform:** AWS (Amazon Web Services).  
>    - **Storage:** Amazon S3 for document handling (PDF, DOCX, TXT).  
>    - **Processing:** AWS Lambda (serverless).  
>    - **Database:** DynamoDB for metadata and query history persistence.  
>  
> 2. **User Interface:**  
>    - **Technology:** Streamlit.  
>    - **Features:** File upload (PDF, DOCX, TXT) and structured summaries of tender requirements.  
>  
> 3. **Text Processing:**  
>    - **Requirement:** Implementation of a text extraction and analysis mechanism using NLP.  
>  
> 4. **Scalability and Performance:**  
>    - **Key Features:**  
>       - High availability.  
>       - Auto Scaling and load balancing.  
>    - **Requirement:** Optimized response times for large query volumes.  
>  
> **### Financial Requirements**  
>  
> 1. **Cost Model:**  
>    - **Strategy:** Pay-as-you-go (usage-based billing).  
>    - **Resource Optimization:** Use of EC2 spot instances to reduce costs.  
>  
> 2. **Initial Budget:**  
>    - **Consideration:** Minimizing operational expenses.  
>    - **Financial Plan:** Structured to ensure sustainability as demand grows.  
>  
> **### Conditions and Requirements**  
>  
> - **Proven experience** in implementing similar projects.  
> - **Support and maintenance requirements** to ensure operational continuity.  
> - **Certification and compliance** with data protection regulations such as **LGPD**.  

Based on the results obtained, it was concluded that the main objective of this sprint was successfully achieved: the LLM instance was correctly configured and used to process and extract requirements from a simulated public tender document.  

---

## **Conclusion**  

The tests demonstrated that the LLM model effectively identified and summarized the technical and financial requirements of the fictitious tender document in a structured manner. While minor variations may occur depending on the input text formulation, the tool successfully met the sprint objective: enabling the instance of an LLM for extracting tender requirements.  

The next phase of the project involves a more in-depth analysis of variations in the generated results as different documents are processed. Additionally, a study will be conducted on optimization techniques for information extraction, ensuring greater precision and ease of access to structured data for the end user. This evolution will enhance the efficiency and scalability of the solution, making it even more effective for the company's sales and pre-sales teams.