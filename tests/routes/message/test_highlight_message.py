from fastapi.testclient import TestClient
import pytest
from requests.models import Response
from src.app import app


client = TestClient(app)


@pytest.fixture()
def message() -> dict:
    message: dict = {
        "recipient_id": "test-recipient",
        "sender_id": "test-sender",
        "timestamp": "2022-06-15T11:00:00"
    }
    return message


@pytest.fixture()
def words_to_highlight() -> list:
    words_to_highlight: list = ["HELLO", "world", "message"]
    return words_to_highlight


def test_empty_message(message, words_to_highlight) -> None:
    message.update(text="")
    response: Response = client.post(
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


def test_clean_message_with_empty_words_to_highlight(message) -> None:
    message.update(text="This is a test message to test the message highlighter.")
    words_to_highlight = []
    response: Response = client.post(
        "/message/highlight",
        json={
            "message": message,
            "words_to_highlight": words_to_highlight,
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        **message,
        "fragments": [
            {
                "is_highlighted": False,
                "text": "This is a test message to test the message highlighter."
            }
        ]
    }


def test_highlightable_message_with_word_to_highlight(message, words_to_highlight) -> None:
    message.update(text="This is a test message to test the message highlighter.")
    response: Response = client.post(
        "/message/highlight",
        json={
            "message": message,
            "words_to_highlight": words_to_highlight,
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        **message,
        "fragments": [
            {
                "is_highlighted": False,
                "text": "This is a test"
            },
            {
                "is_highlighted": True,
                "text": "message"
            },
            {
                "is_highlighted": False,
                "text": "to test the"
            },
            {
                "is_highlighted": True,
                "text": "message"
            },
            {
                "is_highlighted": False,
                "text": "highlighter."
            }
        ]
    }


def test_message_wrong_type_expects_string(message, words_to_highlight) -> None:
    message.update(text=["This is a message inside a list."])
    response: Response = client.post(
        "/message/highlight",
        json={
            "message": message,
            "words_to_highlight": words_to_highlight,
        }
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "str type expected"


def test_message_is_mandatory_field(message, words_to_highlight) -> None:
    response: Response = client.post(
        "/message/highlight",
        json={
            "message": message,
            "words_to_highlight": words_to_highlight,
        }
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"


def test_recipient_is_mandatory_field(message, words_to_highlight) -> None:
    message.update(text="This is a test message to test the message highlighter.")
    message.pop("recipient_id")
    response: Response = client.post(
        "/message/highlight",
        json={
            "message": message,
            "words_to_highlight": words_to_highlight,
        }
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"


def test_sender_is_mandatory_field(message, words_to_highlight) -> None:
    message.update(text="This is a test message to test the message highlighter.")
    message.pop("sender_id")
    response: Response = client.post(
        "/message/highlight",
        json={
            "message": message,
            "words_to_highlight": words_to_highlight,
        }
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"


def test_timestamp_is_mandatory_field(message, words_to_highlight) -> None:
    message.update(text="This is a test message to test the message highlighter.")
    message.pop("timestamp")
    response: Response = client.post(
        "/message/highlight",
        json={
            "message": message,
            "words_to_highlight": words_to_highlight,
        }
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"


def test_timestamp_is_datetime_compliant(message, words_to_highlight) -> None:
    message.update(text="This is a test message to test the message highlighter.")
    message.update(timestamp="this_is_not_a_date")
    response: Response = client.post(
        "/message/highlight",
        json={
            "message": message,
            "words_to_highlight": words_to_highlight,
        }
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "invalid datetime format"
