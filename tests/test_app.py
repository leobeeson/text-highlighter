from fastapi.testclient import TestClient
from src.app import app
from src.version import version

client = TestClient(app)


def test_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "ok": True,
        "version": version,
    }
