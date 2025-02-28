---
title: Requirements Gathering
sidebar_position: 2
slug: /requirements-gathering
---


To ensure the project fully meets the client’s needs, critical requirements were identified during a scoping interview aimed at refining the project’s understanding. These requirements were categorized into two main groups: *functional* and *non-functional*. This division reflects the project’s complexity, which demands both the implementation of core functionalities aligned with minimum standards and adherence to rigorous performance metrics. **Functional Requirements (FRs)** specify the actions and operations the system must perform, while **Non-Functional Requirements (NFRs)** define measurable criteria for optimization, security, scalability, and other quality attributes. Additionally, each requirement was classified as *"mandatory"* (essential for the initial delivery) or *"desirable"* (value-added for future iterations), enabling the team to strategically prioritize implementation in alignment with the client’s objectives.  


## Functional Requirements (FRs)

| ID   | Title                                    | Description                                                                                           | Category   |
|------|-------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------|
| FR1  | Bid Document Processing Performance | The system shall process bid documents (up to 10 MB in size) with an average processing time of ≤5 minutes, measured from upload completion to generation of the final output (technical/financial requirements summary and compliance matching). | Mandatory |
| FR2  | Scalability | The system must be able to process multiple bid documents simultaneously by distributing the workload. | Mandatory |
| FR3  | Security | Data must be securely stored, ensuring file encryption and authenticated access via login.| Desirable   |
| FR4  | Usability | The interface must be intuitive, with a minimal learning curve for sales and pre-sales users. | Desirable |
| FR5  | Logging | A logging mechanism must be in place to track failures, system usage, and user activities, facilitating audits and troubleshooting. | Desirable |


