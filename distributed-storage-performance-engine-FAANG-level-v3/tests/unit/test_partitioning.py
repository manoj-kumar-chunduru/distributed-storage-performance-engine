from storage_engine.partitioning.partitioner import Partitioner

def test_partition_is_deterministic():
    p = Partitioner(16)
    assert p.partition("customer-100") == p.partition("customer-100")
    assert 0 <= p.partition("customer-100") < 16
