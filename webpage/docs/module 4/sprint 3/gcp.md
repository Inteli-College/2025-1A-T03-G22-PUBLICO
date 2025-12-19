# Deploy GCP
## Sprint 18: Load Balancing and Fault Tolerance Implementation

During this sprint, I completed the deployment of the Docker image integrated with the RAG module developed in Sprint 3. This architecture was selected due to its lightweight interface, lower operational cost, and ability to horizontally scale while maintaining predictable performance — essential for the upcoming demonstration.

The deployment was executed using Google Cloud Run, leveraging its fully managed, serverless container environment. I configured an automated deployment pipeline connected to Docker Hub, ensuring that new image versions were pulled and rolled out reliably across the platform.

Cloud Run acted as the primary load-balancing layer, automatically distributing incoming requests across multiple container instances. Autoscaling policies were configured to dynamically provision additional instances based on concurrent request volume, ensuring consistent throughput under variable workloads.

To improve fault tolerance, I enabled health checks and instance-level monitoring provided by Cloud Run. These mechanisms ensure that failing or degraded instances are automatically replaced, preserving service availability without manual intervention. Additionally, the isolation model of Cloud Run containers prevents cascading failures, contributing to the resilience of the overall architecture.

As a result, the application now operates in a robust, scalable, and fault-tolerant environment with reduced latency and better performance guarantees, fully prepared for the upcoming demo and future iterations of the system.