# Expectations

DO NOT SEND THIS DOCUMENT TO ANY CANDIDATES.

## Mandatory tasks

In `src/routes/status.py`, in the `status()`, the `version` should be changed to be loaded from the `src.version` file.

In `src/text_processing/highlight_text.py` the `_highlight_words()` function is not implemented.
The candidate should implement it. The code should be clean, well named, and working.

In `src/text_processing/highlight_text.py` the `lowercase_words_to_highlight` are not actually lowercase. 
The candidate is expected to find this, add tests and fix the problem. It's up to the candidate to come up with a way to do this.
One way to work around this is by adding a lowercase in `src/text_processing/highlight_text` or by doing the same in `src/routes/message/highlight_message`.

The tests in `tests/text_processing/test_highlight_text` are missing any tests for multiple words, and large blocks of highlighted words.
Depending on how the candidate approaches the previous task, they could add tests ensuring that the words list works with uppercase and lowercase words.

The task to fix `src/text_processing/remove_emojis` can be fixed in two ways:
- The lazy way is to simply adjust the end index in that slice operation on line 7
- A better way is to use a `replace()` function from string, as that simplifies the code too

## Optional tasks

The version number is hardcoded in `src/routes/status.py`. It could be loaded from the version.py.

The code in `src/text_processing/test_highlight_message.py` is longer than 100 characters. It should be reformatted.
