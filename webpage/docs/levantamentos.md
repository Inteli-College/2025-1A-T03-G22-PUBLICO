---
title: Requirements Gathering
sidebar_position: 2
slug: /requirements-gathering
---


To ensure the project fully meets the client’s needs, critical requirements were identified during a scoping interview aimed at refining the project’s understanding. These requirements were categorized into two main groups: *functional* and *non-functional*. This division reflects the project’s complexity, which demands both the implementation of core functionalities aligned with minimum standards and adherence to rigorous performance metrics. **Functional Requirements (FRs)** specify the actions and operations the system must perform, while **Non-Functional Requirements (NFRs)** define measurable criteria for optimization, security, scalability, and other quality attributes. Additionally, each requirement was classified as *"mandatory"* (essential for the initial delivery) or *"desirable"* (value-added for future iterations), enabling the team to strategically prioritize implementation in alignment with the client’s objectives.  


## Functional Requirements (FRs)

| ID   | Title                                    | Description                                                                                           | Category   |
|------|-------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------|
| FR1  | Bid Document Processing and Summarization | The system must process bid documents by reading, analyzing, and summarizing their content to automatically extract technical and functional requirements. | Mandatory |
| FR2  | Interactive Results Overview & Export   | The system must dynamically generate a concise summary of key bid document insights and display them in a user-friendly prompt. Additionally, it must enable on-demand export of the summarized results as a PDF for offline access. | Mandatory |
| FR3  | Bid-Compliance Certification Matching| The system must automatically cross-reference bid requirements with the company’s existing certifications to identify and suggest relevant documentation that validates the company’s capability to fulfill the bid’s specific demands. This feature will leverage a vector database to intelligently categorize project types and align them with pre-approved certifications, ensuring contextual relevance.| Desirable   |
| FR4  | Comprehensive Usage History Archiving | The system must securely store all user requests, feedback, and system-generated compliance matches in a structured, searchable repository. This historical data will be aggregated into a centralized data lake, enabling long-term strategic analytics, trend identification, and operational auditability to support data-driven decision-making. | Desirable |
| FR5  | Data Lake Analytics Dashboard |The system must include an interactive analytics interface that enables users to explore, filter, and visualize data from the centralized data lake. This dashboard will display user activity metrics, system performance trends, and compliance match insights through dynamic charts, tables, and customizable filters, empowering stakeholders to derive actionable intelligence and monitor long-term operational efficiency. | Desirable |


