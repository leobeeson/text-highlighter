from src.text_processing.highlight_text import TextWithHighlights, TextFragmentWithHighlights


def pytest_assertrepr_compare(op, left, right):
    if (
        isinstance(left, TextWithHighlights)
        and isinstance(right, TextWithHighlights)
        and op == "=="
    ):
        return [
            "Comparing TextWithHighlights instances:",
            *str(left).split("\n"),
            '!=',
            *str(right).split("\n"),
        ]
