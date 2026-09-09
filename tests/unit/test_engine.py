from storage_engine.core.engine import StorageEngine
from storage_engine.storage.backend import InMemoryStorage


def test_idempotent_write():
    e = StorageEngine(InMemoryStorage())
    assert e.put("a", 1, "req-1")["status"] == "stored"
    assert e.put("a", 1, "req-1")["status"] == "duplicate"
