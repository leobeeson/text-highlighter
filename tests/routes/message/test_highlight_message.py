from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_empty_message():
    message = {
        "recipient_id": "test-recipient",
        "sender_id": "test-sender",
        "text": "",
        "timestamp": "2022-06-15T11:00:00",
    }
    words_to_highlight = ["HELLO", "world"]
    response = client.post(
        "/message/highlight",
        json={
            "message": message,
            "words_to_highlight": words_to_highlight,
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        **message,
        "fragments": [],
    }

# TODO: Add more tests here
