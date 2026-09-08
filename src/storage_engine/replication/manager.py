class ReplicationManager:
    def __init__(self, replicas=None):
        self.replicas = replicas or []

    def replicate_put(self, key, value):
        successes = 0
        for replica in self.replicas:
            try:
                replica.put(key, value)
                successes += 1
            except Exception:
                pass
        return successes

    def replicate_delete(self, key):
        successes = 0
        for replica in self.replicas:
            try:
                if replica.delete(key):
                    successes += 1
            except Exception:
                pass
        return successes
