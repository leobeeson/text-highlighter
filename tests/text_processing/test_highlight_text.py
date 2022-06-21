from src.text_processing.highlight_text import (
    highlight_text,
    TextFragmentWithHighlights,
    TextWithHighlights,
)


def test_empty_text() -> None:
    result: TextWithHighlights = highlight_text("", [])
    assert result == TextWithHighlights([])


def test_text_with_empty_words() -> None:
    message: str = "This is a test message to test the message highlighter."
    result: TextWithHighlights = highlight_text(message, [])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights(
            message, 
            is_highlighted=False
        )
    ])


def test_text_with_multiple_spaces() -> None:
    message: str = "This message has   multiple  spaces between  words."
    result: TextWithHighlights = highlight_text(message, [])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights(
            "This message has multiple spaces between words.", 
            is_highlighted=False
        )
    ])


def test_different_case_words() -> None:
    message: str = "Hello hello HeLLo HELLO"
    result: TextWithHighlights = highlight_text(message, ["hello"])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights(
            message, 
            is_highlighted=True
        )
    ])


def test_words_in_multiple_groups() -> None:
    message:str = "Hello World! hello world! HeLLo WoRlD! HELLO WORLD!"
    result: TextWithHighlights = highlight_text(message, ["hello"])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights("Hello", is_highlighted=True),
        TextFragmentWithHighlights("World!", is_highlighted=False),
        TextFragmentWithHighlights("hello", is_highlighted=True),
        TextFragmentWithHighlights("world!", is_highlighted=False),
        TextFragmentWithHighlights("HeLLo", is_highlighted=True),
        TextFragmentWithHighlights("WoRlD!", is_highlighted=False),
        TextFragmentWithHighlights("HELLO", is_highlighted=True),
        TextFragmentWithHighlights("WORLD!", is_highlighted=False),
    ])


def test_clean_message_with_word_to_highlight_in_upper_case() -> None:
    message: str = "This message has   multiple  spaces between  words."
    result: TextWithHighlights = highlight_text(message, ["HELLO"])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights(
            "This message has multiple spaces between words.", 
            is_highlighted=False
        )
    ])


def test_highlightable_message_with_word_to_highlight_in_upper_case() -> None:
    message: str = "This message has   multiple  spaces between  words. Hello World!"
    result: TextWithHighlights = highlight_text(message, ["HELLO"])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights(
            "This message has multiple spaces between words.", 
            is_highlighted=False
        ),
        TextFragmentWithHighlights(
            "Hello", 
            is_highlighted=True
        ),
        TextFragmentWithHighlights(
            "World!", 
            is_highlighted=False
        )
    ])


def test_highlightable_message_with_all_words_to_highlight_present_in_message() -> None:
    message: str = "This is a test message to test the message highlighter. Hello World!"
    result: TextWithHighlights = highlight_text(message, ["message", "hello"])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights("This is a test", is_highlighted=False),
        TextFragmentWithHighlights("message", is_highlighted=True),
        TextFragmentWithHighlights("to test the", is_highlighted=False),
        TextFragmentWithHighlights("message", is_highlighted=True),
        TextFragmentWithHighlights("highlighter.", is_highlighted=False),
        TextFragmentWithHighlights("Hello", is_highlighted=True),
        TextFragmentWithHighlights("World!", is_highlighted=False),
    ])


def test_highlightable_message_with_some_words_to_highlight_present_in_message() -> None:
    message: str = "This is a test message to test the message highlighter. Hello World!"
    result: TextWithHighlights = highlight_text(
        message, 
        ["message", "supercalifragilisticexpialidocious"]
    )
    assert result == TextWithHighlights([
        TextFragmentWithHighlights("This is a test", is_highlighted=False),
        TextFragmentWithHighlights("message", is_highlighted=True),
        TextFragmentWithHighlights("to test the", is_highlighted=False),
        TextFragmentWithHighlights("message", is_highlighted=True),
        TextFragmentWithHighlights("highlighter. Hello World!", is_highlighted=False),
    ])


def test_clean_message_with_all_words_to_highlight_not_present_in_message() -> None:
    message: str = "This is a test message to test the message highlighter. Hello World!"
    result: TextWithHighlights = highlight_text(
        message, 
        ["catchmeifyoucan", "supercalifragilisticexpialidocious"]
    )
    assert result == TextWithHighlights([
        TextFragmentWithHighlights(
            "This is a test message to test the message highlighter. Hello World!", 
            is_highlighted=False
            )
    ])


def test_highlightable_message_with_multiword_to_highlight_present_in_message() -> None:
    message: str = "This is a test message to test the message highlighter. Also, hello world!"
    result: TextWithHighlights = highlight_text(
        message, 
        ["message highlighter.", "hello world!"]
    )
    assert result == TextWithHighlights([
        TextFragmentWithHighlights("This is a test message to test the", is_highlighted=False),
        TextFragmentWithHighlights("message highlighter.", is_highlighted=True),
        TextFragmentWithHighlights("Also,", is_highlighted=False),
        TextFragmentWithHighlights("hello world!", is_highlighted=True),
    ])


def test_highlightable_message_with_uppercase_multiword_to_highlight_present_in_message() -> None:
    message: str = "This is a test message to test the message highlighter. Also, HELLO WORLD!"
    result: TextWithHighlights = highlight_text(
        message, 
        ["message highlighter.", "hello world!"]
    )
    assert result == TextWithHighlights([
        TextFragmentWithHighlights("This is a test message to test the", is_highlighted=False),
        TextFragmentWithHighlights("message highlighter.", is_highlighted=True),
        TextFragmentWithHighlights("Also,", is_highlighted=False),
        TextFragmentWithHighlights("HELLO WORLD!", is_highlighted=True),
    ])


def test_highlightable_message_with_propercase_multiword_to_highlight_present_in_message() -> None:
    message: str = "This is a test message to test the message highlighter. Also, Hello World!"
    result: TextWithHighlights = highlight_text(
        message, 
        ["message highlighter.", "hello world!"]
    )
    assert result == TextWithHighlights([
        TextFragmentWithHighlights("This is a test message to test the", is_highlighted=False),
        TextFragmentWithHighlights("message highlighter.", is_highlighted=True),
        TextFragmentWithHighlights("Also,", is_highlighted=False),
        TextFragmentWithHighlights("Hello World!", is_highlighted=True),
    ])

def test_highlightable_message_with_lowercase_multiword_to_highlight_present_in_message() -> None:
    message: str = "This is a test message to test the message highlighter. Also, hello world!"
    result: TextWithHighlights = highlight_text(
        message, 
        ["message highlighter.", "Hello world!"]
    )
    assert result == TextWithHighlights([
        TextFragmentWithHighlights("This is a test message to test the", is_highlighted=False),
        TextFragmentWithHighlights("message highlighter.", is_highlighted=True),
        TextFragmentWithHighlights("Also,", is_highlighted=False),
        TextFragmentWithHighlights("hello world!", is_highlighted=True),
    ])
