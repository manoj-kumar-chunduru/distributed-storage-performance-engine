from storage_engine.storage.backend import InMemoryStorage


def test_storage_lifecycle():
    s = InMemoryStorage()
    s.put("a", {"value": 1})
    assert s.get("a") == {"value": 1}
    assert s.delete("a")
    assert s.get("a") is None
