# Distributed Storage Performance Engine

A production-oriented distributed storage engine demonstrating high-throughput I/O,
concurrent request processing, partitioning, caching, replication concepts,
observability, benchmarking, and fault-tolerant backend design.

## Overview
This project models large-scale storage engineering challenges: efficient data access,
predictable latency, horizontal scalability, concurrency, failure handling, and measurable performance.

## Architecture
```text
Clients
   |
   v
Storage API -> Storage Coordinator
                  |       |       |
                  v       v       v
             Partition  Cache  Replication
                  |
                  v
             Storage Backend
                  |
                  v
               Metrics
```

## Tech Stack
- Python 3.11+
- FastAPI / Pydantic
- pytest / Ruff
- Docker / Kubernetes
- GitHub Actions
- Prometheus-compatible metrics

## Key Features
- Thread-safe storage operations
- Deterministic partition-aware routing
- TTL in-memory cache
- Pluggable storage backend
- Replication abstraction
- Idempotent writes
- Health/readiness endpoints
- Metrics endpoint
- Unit, integration, and concurrency tests
- Repeatable throughput/latency benchmark
- Non-root Docker container
- Kubernetes deployment baseline
- Architecture Decision Record

## API Examples
```bash
curl http://localhost:8000/health

curl -X PUT http://localhost:8000/v1/objects/customer-1001   -H "Content-Type: application/json"   -d '{"value":{"tier":"gold","region":"us-east"}}'

curl http://localhost:8000/v1/objects/customer-1001

curl -X DELETE http://localhost:8000/v1/objects/customer-1001

curl http://localhost:8000/metrics
```

## Project Structure
```text
src/storage_engine/
├── api/             # HTTP API
├── cache/           # TTL cache
├── core/            # Storage coordinator
├── partitioning/    # Deterministic routing
├── replication/     # Replica abstraction
├── storage/         # Backend interface
└── metrics/         # Runtime metrics
tests/
├── unit/
├── integration/
└── performance/
benchmarks/
docs/
k8s/
.github/workflows/
```

## Running Locally
```bash
python -m venv .venv
```

Windows:
```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Install and run:
```bash
pip install -e ".[dev]"
uvicorn storage_engine.api.app:app --host 0.0.0.0 --port 8000
```

Or:
```bash
make run
```

## Docker
```bash
docker compose up --build
```

## Testing
```bash
pytest -q
ruff check .
```

Concurrency test:
```bash
pytest tests/performance -q
```

## Benchmarking
```bash
python benchmarks/benchmark.py
```

Reports:
- operations/second
- average latency
- p50
- p95
- p99

Results are workload- and hardware-dependent. Synthetic local measurements are not represented as production achievements.

## Observability
Endpoints:
- `/health`
- `/ready`
- `/metrics`

Tracked signals include requests, errors, cache hits/misses, latency, and object count.

## CI/CD
GitHub Actions performs dependency installation, linting, tests, and benchmark smoke execution.
A production pipeline can extend this with SBOM generation, image scanning, signing, deployment promotion, and rollback.

## Reliability & Scalability
The design separates routing, storage, caching, and replication so each concern can evolve independently.

Production evolution:
- durable WAL
- quorum replication
- replica health tracking
- backpressure
- circuit breakers
- graceful shutdown
- snapshots/recovery
- chaos testing

## Security
Production deployments should add OAuth/OIDC or service identity, TLS/mTLS, network policies,
least-privilege IAM, secrets management, audit logging, rate limits, and dependency/image scanning.

## Engineering Principles
- Measure before optimizing
- Design for failure
- Keep concurrency testable
- Prefer explicit interfaces
- Automate validation
- Document architectural trade-offs
- Separate benchmark evidence from production claims

## Future Improvements
- WAL-backed persistence
- LSM-tree/SSTable engine
- Consistent hashing
- Quorum replication
- Background compaction
- Snapshot/restore
- OpenTelemetry tracing
- StatefulSet deployment
- Chaos/fault-injection testing

## Author
**Manoj Kumar Chunduru**  
Software Engineer
