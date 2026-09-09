from fastapi.testclient import TestClient

from storage_engine.api.app import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_lifecycle():
    assert client.put("/v1/objects/demo", json={"value": {"hello": "world"}}).status_code == 200
    assert client.get("/v1/objects/demo").json()["value"] == {"hello": "world"}
    assert client.delete("/v1/objects/demo").json()["deleted"] is True
