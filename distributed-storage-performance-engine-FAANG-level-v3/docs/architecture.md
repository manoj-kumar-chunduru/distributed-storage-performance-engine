# Architecture

The storage coordinator composes routing, caching, persistence, replication, and metrics.

The API validates requests; partitioning determines a deterministic shard; reads consult
cache before storage; writes update storage/cache and invoke replication.

The modular design keeps performance experiments and backend replacement isolated.
