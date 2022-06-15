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
        TextFragmentWithHighlights("This message has multiple spaces between words.", is_highlighted=False)
    ])
