from abc import ABC, abstractmethod
from threading import RLock
from typing import Any


class StorageBackend(ABC):
    @abstractmethod
    def put(self, key: str, value: Any) -> None: ...
    @abstractmethod
    def get(self, key: str) -> Any | None: ...
    @abstractmethod
    def delete(self, key: str) -> bool: ...


class InMemoryStorage(StorageBackend):
    def __init__(self):
        self._data = {}
        self._lock = RLock()

    def put(self, key, value):
        with self._lock:
            self._data[key] = value

    def get(self, key):
        with self._lock:
            return self._data.get(key)

    def delete(self, key):
        with self._lock:
            return self._data.pop(key, None) is not None

    def size(self):
        with self._lock:
            return len(self._data)
