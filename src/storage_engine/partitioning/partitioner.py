from hashlib import sha256


class Partitioner:
    def __init__(self, partitions=16):
        if partitions < 1:
            raise ValueError("partitions must be positive")
        self.partitions = partitions

    def partition(self, key):
        digest = sha256(key.encode()).digest()
        return int.from_bytes(digest[:8], "big") % self.partitions
