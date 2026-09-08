from time import perf_counter
from statistics import mean
from storage_engine.core.engine import StorageEngine
from storage_engine.storage.backend import InMemoryStorage

def pct(values, p):
    values = sorted(values)
    return values[min(len(values)-1, int(len(values)*p))]

engine = StorageEngine(InMemoryStorage())
latencies = []
operations = 10000
start = perf_counter()
for i in range(operations):
    t = perf_counter()
    key = f"key-{i % 1000}"
    engine.put(key, {"value": i})
    engine.get(key)
    latencies.append((perf_counter()-t)*1000)
elapsed = perf_counter()-start
print(f"operations: {operations}")
print(f"throughput_ops_sec: {operations/elapsed:.2f}")
print(f"avg_latency_ms: {mean(latencies):.3f}")
print(f"p50_latency_ms: {pct(latencies,.50):.3f}")
print(f"p95_latency_ms: {pct(latencies,.95):.3f}")
print(f"p99_latency_ms: {pct(latencies,.99):.3f}")
