from src.text_processing.highlight_text import (
    highlight_text,
    TextFragmentWithHighlights,
    TextWithHighlights,
)


def test_empty_text():
    result = highlight_text("", [])
    assert result == TextWithHighlights([])


def test_text_with_empty_words():
    message = "This is a test message to test the message highlighter."
    result = highlight_text(message, [])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights(message, is_highlighted=False)
    ])


def test_text_with_multiple_spaces():
    message = "This message has   multiple  spaces between  words."
    result = highlight_text(message, [])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights("This message has multiple spaces between words.", is_highlighted=False),
    ])


def test_different_case_words():
    message = "Hello hello HeLLo HELLO"
    result = highlight_text(message, ["hello"])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights(message, is_highlighted=True),
    ])


def test_words_in_multiple_groups():
    message = "Hello World! hello world! HeLLo WoRlD! HELLO WORLD!"
    result = highlight_text(message, ["hello"])
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


def test_clean_message_with_word_to_highlight_in_upper_case():
    message = "This message has   multiple  spaces between  words."
    result = highlight_text(message, ["HELLO"])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights("This message has multiple spaces between words.", is_highlighted=False),
    ])


def test_highlightable_message_with_word_to_highlight_in_upper_case():
    message = "This message has   multiple  spaces between  words. Hello World!"
    result = highlight_text(message, ["HELLO"])
    assert result == TextWithHighlights([
        TextFragmentWithHighlights("This message has multiple spaces between words.", is_highlighted=False),
        TextFragmentWithHighlights("Hello", is_highlighted=True),
        TextFragmentWithHighlights("World!", is_highlighted=False),
    ])
