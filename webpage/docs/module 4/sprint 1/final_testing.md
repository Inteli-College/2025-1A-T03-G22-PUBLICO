
# Infrastructure Optimization
## Sprint 16: Optimization of the infrastructure to support high demand

Objective of the sprint
Ensure the LLM-based tender analysis platform operates with low latency, high availability, and controlled cost under usage spikes, especially near tender deadlines. The sprint focuses on horizontal scalability, workload isolation (OCR, indexing, inference), capacity automation, observability, resilience, and security.

### Load context and assumptions
- Usage profile: spikes near public tender deadlines; multiple concurrent analyses by sales and pre-sales squads.
- Document size: up to 200+ pages; some requiring OCR.
- Pipeline: upload → extraction/normalization → chunking/embeddings → indexing → RAG → LLM inference → cross-check with attestations → report.
- Expected bottlenecks: OCR/extraction, large-scale embedding generation, vector search over large collections, and LLM inference.

### Non-functional requirements (proposed SLOs)
- Response latency:
  - Initial response (summary + preliminary requirements): ≤ 180 s.
  - Full report (including cross-check with attestations): ≤ 5 min for tenders up to 200 pages.
- Availability: ≥ 90% monthly.
- Reliability: processing failure rate < 10% (with automatic reprocessing via queue).
- Cost: ≥ 25% reduction in cost per document versus the previous baseline (via autoscaling/caching).

### Target architecture (macro view)
- Orchestration: Managed Kubernetes (EKS/GKE/AKS) with:
  - HPA/VPA and Cluster Autoscaler.
  - KEDA for scaling based on queue metrics.
- Layers and services (microservices decoupled by queues/asynchronicity):
  1) Ingestion/Upload + antivirus + integrity checks.
  2) Extraction/OCR (CPU-optimized; GPU only if needed).
  3) Normalization/Chunking and deduplication.
  4) Embeddings (optional GPU; batching and cache).
  5) Indexing and RAG (Vector DB partitioned by client/project).
  6) LLM serving (vLLM/TensorRT-LLM) with continuous batching and PagedAttention.
  7) Cross-check against company attestations (transactional service + hot cache).
  8) Report generation and delivery to the user.
- Messaging and queues: RabbitMQ/Kafka/PubSub for backpressure, DLQ, and reprocessing.
- Storage:
  - Objects (tenders and artifacts): S3/Blob with versioning and lifecycle policies.
  - Metadata/Transactional: Managed PostgreSQL (RDS/CloudSQL).
  - Vector: Milvus/Weaviate/pgvector/Elasticsearch with HNSW/IVF, sharding, and replication.
- API Gateway and security: rate limiting, quotas, WAF, TLS, JWT/OIDC, tenant isolation.
- Observability: Prometheus/Grafana + OpenTelemetry (tracing) + ELK/OpenSearch + Sentry.

### Scalability and performance strategies
- Separation of control and data planes: control infra (APIs, auth, dashboard) isolated from heavy pipeline (OCR, embeddings, LLM).
- Autoscaling:
  - HPA by CPU/RAM; for async jobs, scale by queue depth (KEDA).
  - Warm GPU pools for LLM serving (warm starts) and spot nodes with on-demand fallback.
- LLM serving:
  - vLLM with continuous batching, tuning of max_tokens and parallelism.
  - Quantization (fp16/int8) when applicable without critical quality loss.
  - Prompt/result caching keyed by content hash + parameters.
- RAG/Indexing:
  - Asynchronous preprocessing; store embeddings with chunk hash for reuse.
  - Index partitioning by client/tender and read replicas.
  - HNSW with ef/efConstruction tuning to balance recall/latency.
  - Page/segment deduplication and vector compression (IVF-PQ when applicable).
- OCR and extraction:
  - CPU-first pipeline, controlled concurrency, and a dedicated queue for OCR documents.
  - Priority/fairness: prevent a huge tender from blocking many small ones (fair queue).
- Multilayer caching:
  - Final results by tender hash.
  - Cache for embeddings and vector-search top‑k for repeated queries.
  - CDN for static frontend assets.
- Reliability:
  - Idempotent retries, per-stage DLQ, circuit breakers, timeouts, and backoff policies.
  - Health probes (liveness/readiness) and zone-failure tolerance.
- Cost:
  - Spot GPUs with fallback, automatic shutdown of idle nodes.
  - Object lifecycle policies (tiering), artifact/log compression.
  - Rightsizing via VPA and proper requests/limits.

### Observability and SRE
- Key metrics:
  - p50/p95 latency per stage (OCR, embeddings, RAG, LLM).
  - Queue depth, reprocessing rate, time-to-drain.
  - GPU/CPU/RAM utilization per pod; OOMs and error rates by type.
  - Vector DB latency and QPS; cache hit rate.
- Distributed tracing: end-to-end correlation by document/execution ID.
- Dashboards and alerts:
  - Alerts for p95 above SLO for X minutes; queue depth above N; GPU > 90% for Y minutes; cascading failures.
- Runbooks: mitigation, rollback, and contingency procedures.

### Deliverables
- Observability:
  - Stage-specific Grafana dashboards; Prometheus alerts; OpenTelemetry traces.
  - Sentry/ELK configured with sensitive data filtering.
- Operations:
  - Tested backup/restore policies.
- Quality:
  - Load and resilience test report with baseline comparison.
  - Capacity plan and cost per document.

### Acceptance criteria
- Initial summary within 120 s (p95) and full report within 5 min (p95).
- Controlled performance degradation under 5x spike with automatic recovery via autoscaling.
- Availability ≥ 90% during the validation period and zero data loss under injected failures.
- ≥ 25% reduction in cost per document relative to the previous baseline.
- Dashboards and alerts active; runbooks approved by operations.

### Risks and mitigation
- Scarcity or preemption of spot GPUs: maintain a minimum on‑demand pool and fallback orchestration.
- Cost spikes during peaks: autoscaling limits, per-tenant quotas, aggressive caching, and data lifecycle policies.
- Recall degradation in RAG after compression/parameter tuning: A/B testing with validation sets and quality monitoring.
- Vendor lock-in: compatible abstractions (Helm/Terraform), open-source components, and compatibility layers.

### Expected benefits
- Faster and more consistent responses, especially in critical periods.
- Operational predictability with mature observability and autoscaling.
- Lower cost per document via caching, batching, and efficient GPU/CPU usage.
- Greater resilience and security, aligned with LGPD and public-sector requirements.

Finally, as this is an MVP, these implementations will not be carried out in this phase, but the in‑depth architectural study is valuable for the project’s continuity.