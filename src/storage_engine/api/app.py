from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from storage_engine.cache.ttl_cache import TTLCache
from storage_engine.core.engine import StorageEngine
from storage_engine.storage.backend import InMemoryStorage

app = FastAPI(title="Distributed Storage Performance Engine", version="0.1.0")
metrics = {"requests": 0, "errors": 0}
backend = InMemoryStorage()
engine = StorageEngine(backend, TTLCache(30), metrics=metrics)

class ObjectRequest(BaseModel):
    value: object
    request_id: str | None = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.put("/v1/objects/{key}")
def put_object(key: str, request: ObjectRequest):
    return engine.put(key, request.value, request.request_id)

@app.get("/v1/objects/{key}")
def get_object(key: str):
    value, cached = engine.get(key)
    if value is None:
        raise HTTPException(404, "object not found")
    return {"key": key, "value": value, "cache_hit": cached}

@app.delete("/v1/objects/{key}")
def delete_object(key: str):
    return {"deleted": engine.delete(key)}

@app.get("/metrics")
def get_metrics():
    return {**metrics, "cache_hits": engine.cache.hits, "cache_misses": engine.cache.misses,
            "stored_objects": backend.size()}
