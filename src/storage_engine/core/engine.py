from storage_engine.cache.ttl_cache import TTLCache
from storage_engine.partitioning.partitioner import Partitioner
from storage_engine.replication.manager import ReplicationManager


class StorageEngine:
    def __init__(self, backend, cache=None, partitioner=None, replication=None, metrics=None):
        self.backend = backend
        self.cache = cache or TTLCache()
        self.partitioner = partitioner or Partitioner()
        self.replication = replication or ReplicationManager()
        self.metrics = metrics
        self._idempotency = set()

    def put(self, key, value, request_id=None):
        try:
            if request_id and request_id in self._idempotency:
                return {"status": "duplicate", "partition": self.partitioner.partition(key)}
            self.backend.put(key, value)
            self.cache.put(key, value)
            replicas = self.replication.replicate_put(key, value)
            if request_id:
                self._idempotency.add(request_id)
            return {
                "status": "stored",
                "partition": self.partitioner.partition(key),
                "replicas": replicas,
            }
        except Exception:
            if self.metrics:
                self.metrics["errors"] += 1
            raise
        finally:
            if self.metrics:
                self.metrics["requests"] += 1

    def get(self, key):
        value = self.cache.get(key)
        if value is not None:
            return value, True
        return self.backend.get(key), False

    def delete(self, key):
        deleted = self.backend.delete(key)
        self.cache.invalidate(key)
        self.replication.replicate_delete(key)
        return deleted
