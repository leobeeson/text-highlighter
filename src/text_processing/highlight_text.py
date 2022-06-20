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


def highlight_text(text: str, words_to_highlight: list[str]) -> TextWithHighlights:
    words_to_highlight = _lowercase_words_to_highlight(words_to_highlight)
    fragments = flow(
        text,
        _tokenise_text,
        _create_word_highlighter(words_to_highlight),
    )
    return TextWithHighlights(fragments)


def _create_word_highlighter(words_to_highlight: list[str]) -> Callable[[list[str]], list[TextFragmentWithHighlights]]:
    def word_highlighter(words: list[str]) -> list[TextFragmentWithHighlights]:
        return _highlight_words(words, words_to_highlight)
    return word_highlighter


def _highlight_words(words: list[str], words_to_highlight: list[str]) -> list[TextFragmentWithHighlights]:
    fragments: list[TextFragmentWithHighlights] = []
    if len(words) > 0:
        if len(words_to_highlight) > 0:
            fragments = _build_highlightable_fragments(words, words_to_highlight)
        else:
            fragments = _build_unhighlightable_fragment(words)
    return fragments


def _build_highlightable_fragments(words: list[str], words_to_highlight: list[str]) -> list[TextFragmentWithHighlights]:
    fragments: list[TextFragmentWithHighlights] = []
    fragment_builder: str = ""
    fragment_highlighted: bool = None
    for word in words:
        if word.lower() in words_to_highlight:
            if len(fragment_builder) == 0:
                fragment_highlighted = True
                fragment_builder = word
                continue
            if fragment_highlighted:
                fragment_builder = f"{fragment_builder} {word}"
                continue
            if not fragment_highlighted:
                fragment = TextFragmentWithHighlights(text=fragment_builder, is_highlighted=False)
                fragments.append(fragment)
                fragment_highlighted = True
                fragment_builder = word
        if word.lower() not in words_to_highlight:
            if len(fragment_builder) == 0:
                fragment_highlighted = False
                fragment_builder = word
                continue
            if not fragment_highlighted:
                fragment_builder = f"{fragment_builder} {word}"
                continue
            if fragment_highlighted:
                fragment = TextFragmentWithHighlights(text=fragment_builder, is_highlighted=True)
                fragments.append(fragment)
                fragment_highlighted = False
                fragment_builder = word
    if len(fragment_builder) > 0:
        fragment = TextFragmentWithHighlights(text=fragment_builder, is_highlighted=fragment_highlighted)
        fragments.append(fragment)
    return fragments


def _build_unhighlightable_fragment(words: list[str]) -> list[TextFragmentWithHighlights]:
    fragments = []
    fragment = TextFragmentWithHighlights(text=" ".join(words), is_highlighted=False)
    fragments.append(fragment)
    return fragments


def _tokenise_text(text: str) -> list[str]:
    return text.split()


def _lowercase_words_to_highlight(words_to_highlight: list[str]) -> list[str]:
    return [word.lower() for word in words_to_highlight]
