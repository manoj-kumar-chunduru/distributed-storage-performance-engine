from storage_engine.cache.ttl_cache import TTLCache


def test_cache():
    c = TTLCache(10)
    assert c.get("missing") is None
    c.put("key", "value")
    assert c.get("key") == "value"
    assert c.hits == 1
    assert c.misses == 1
