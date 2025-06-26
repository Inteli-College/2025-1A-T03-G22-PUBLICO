---
title: Frontend Test  
sidebar_position: 3  
slug: /frontend-test  
---

During this sprint, user tests were conducted with both experienced users and those unfamiliar with the system, aiming to assess whether the platform was as intuitive as intended. The test involved asking users to locate a document on their computer, upload it to the platform, select a language model, and interact with it to extract as much information as possible.

Overall, the test was a success. The widespread adoption of tools like ChatGPT and other language models (LLMs) around the world has made users more familiar with this type of interface, greatly facilitating the user experience.

However, one important point of concern was model selection. We observed that users tend to choose one of the first models listed, regardless of their specific characteristics or areas of specialization. This behavior may compromise the results, especially considering that current models are designed for more focused and specific purposes.

Additionally, the test revealed a critical issue: the lack of a clear and standardized initial prompt in each chat. Without this guidance, each user ends up asking different questions for the same document, leading to inconsistencies in the extracted data. This makes it difficult to compare interactions and undermines the accuracy and reliability of the analysis.

To address this issue, it is necessary to implement a fixed prompt that is automatically applied to all chats, regardless of the selected model. This will ensure that all users have a consistent starting point, leading to more uniform and comparable results.