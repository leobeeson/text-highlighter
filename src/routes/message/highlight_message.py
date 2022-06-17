
from fastapi import APIRouter
from typing import List
from ...models.message import Message
from ...text_processing.highlight_text import highlight_text

highlight_message_router = APIRouter()


@highlight_message_router.post("/highlight")
def highlight_message(message: Message, words_to_highlight: List[str]):
    highlighted_message = highlight_text(
        text=message.text,
        lowercase_words_to_highlight=words_to_highlight,
    )
    return {
        **vars(message),
        **vars(highlighted_message),
    }
