
from fastapi import APIRouter
from fastapi import HTTPException
from typing import List
from typing import Union
from ...models.message import Message
from ...text_processing.highlight_text import highlight_text

highlight_message_router = APIRouter()


@highlight_message_router.post("/highlight")
def highlight_message(message: Message, words_to_highlight: List[str]):
    if _some_words_are_numbers(words_to_highlight):
        raise HTTPException(
            status_code=422, 
            detail="words to highlight can't be integers"
        )
    highlighted_message = highlight_text(
        text=message.text,
        words_to_highlight=words_to_highlight,
    )
    return {
        **vars(message),
        **vars(highlighted_message),
    }


def _deserialize_numbers(serialized_list: List[str]) -> List[Union[str, int, float]]:
    deserialized_list: List[Union[str, int, float]]  = []
    for list_element in serialized_list:
        if list_element.isdigit():
            deserialized_list.append(int(list_element))
        else:
            try:
                float(list_element)
                deserialized_list.append(float(list_element))
            except ValueError:
                deserialized_list.append(list_element)
    return deserialized_list


def _some_words_are_numbers(words_to_highlight: List[str]) -> bool:
    words_to_highlight = _deserialize_numbers(words_to_highlight)
    return not all(isinstance(item, str) for item in words_to_highlight)
