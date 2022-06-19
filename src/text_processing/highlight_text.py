from returns.pipeline import flow
from typing import Callable


class TextFragmentWithHighlights:
    is_highlighted: bool
    text: str

    def __init__(self, text: str, is_highlighted: bool):
        self.is_highlighted = is_highlighted
        self.text = text

    def __eq__(self, other: 'TextFragmentWithHighlights') -> bool:
        return (
            self.text == other.text
            and self.is_highlighted == other.is_highlighted
        )

    def __str__(self):
        return f"TextFragmentWithHighlights(text=\"{self.text}\", is_highlighted={self.is_highlighted})"


class TextWithHighlights:
    fragments: list[TextFragmentWithHighlights]

    def __init__(self, fragments: list[TextFragmentWithHighlights]):
        self.fragments = fragments

    def __eq__(self, other: 'TextWithHighlights') -> bool:
        return self.fragments == other.fragments

    def __str__(self) -> str:
        return "\n".join([
            "TextWithHighlights(fragments=[",
            *[f"    {fragment}" for fragment in self.fragments],
            "])",
        ])


def highlight_text(text: str, lowercase_words_to_highlight: list[str]) -> TextWithHighlights:
    fragments = flow(
        text,
        _tokenise_text,
        _create_word_highlighter(lowercase_words_to_highlight),
    )
    return TextWithHighlights(fragments)


def _create_word_highlighter(lowercase_words_to_highlight: list[str]) -> Callable[[list[str]], list[TextFragmentWithHighlights]]:
    def word_highlighter(words: list[str]) -> list[TextFragmentWithHighlights]:
        return _highlight_words(words, lowercase_words_to_highlight)
    return word_highlighter


def _highlight_words(words: list[str], lowercase_words_to_highlight: list[str]) -> list[TextFragmentWithHighlights]:
    fragments = []
    if len(lowercase_words_to_highlight) > 0:
        for word in words:
            if word.lower() in lowercase_words_to_highlight:
                fragment = TextFragmentWithHighlights(text=word, is_highlighted=True)
            else:
                fragment = TextFragmentWithHighlights(text=word, is_highlighted=False)
            fragments.append(fragment)
    else:
        fragment = TextFragmentWithHighlights(text=" ".join(words), is_highlighted=False)
        fragments.append(fragment)
    return fragments


def _tokenise_text(text: str) -> list[str]:
    return text.split()
