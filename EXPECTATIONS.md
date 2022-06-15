# Expected changes

DO NOT SEND THIS DOCUMENT TO ANY CANDIDATES.

In `src/routes/status.py`, in the `status()`, the `version` should be changed to be loaded from the `src.version` file.

In `src/text_processing/highlight_text.py` the `_highlight_words()` function is not implemented.
The candidate should implement it. The code should be clean, well named, and working.

In `src/text_processing/highlight_text.py` the `lowercase_words_to_highlight` are not actually lowercase. 
The candidate is expected to find this, add tests and fix the problem. It's up to the candidate to come up with a way to do this.

