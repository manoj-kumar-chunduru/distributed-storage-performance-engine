from concurrent.futures import ThreadPoolExecutor
from storage_engine.core.engine import StorageEngine
from storage_engine.storage.backend import InMemoryStorage

def test_concurrent_writes():
    e = StorageEngine(InMemoryStorage())
    with ThreadPoolExecutor(max_workers=16) as pool:
        list(pool.map(lambda i: e.put(f"key-{i}", i), range(500)))
    assert e.backend.size() == 500
