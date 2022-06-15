import pytest
from src.text_processing.remove_emojis import remove_emojis

BANNED_EMOJIS = [
    "🏋️",
    "❤️",
    "💩",
]

@pytest.mark.parametrize("test_input,expected", [
    ("", ""),
    ("This contains a valid 🥳 emoji", "This contains a valid 🥳 emoji"),
    ("But contains a banned ❤️ emoji", "But contains a banned  emoji"),
    ("Is this the last test case? 🏋️ who cares", "Is this the last test case?  who cares")
])
def test_remove_emojis(test_input: str, expected: str):
    result = remove_emojis(test_input, BANNED_EMOJIS)
    assert result == expected
