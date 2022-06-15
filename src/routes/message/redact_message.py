
from fastapi import APIRouter
from ...models.message import Message

redact_message_router = APIRouter()


@redact_message_router.post("/redact")
def redact_message(message: Message):
    return {
        "redacted_text": message.text
    }
