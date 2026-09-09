from threading import RLock
from time import monotonic


class TTLCache:
    def __init__(self, ttl_seconds=30.0):
        self.ttl_seconds = ttl_seconds
        self._items = {}
        self._lock = RLock()
        self.hits = 0
        self.misses = 0

    def get(self, key):
        with self._lock:
            item = self._items.get(key)
            if item is None:
                self.misses += 1
                return None
            expires, value = item
            if monotonic() >= expires:
                self._items.pop(key, None)
                self.misses += 1
                return None
            self.hits += 1
            return value

    def put(self, key, value):
        with self._lock:
            self._items[key] = (monotonic() + self.ttl_seconds, value)

    def invalidate(self, key):
        with self._lock:
            self._items.pop(key, None)
