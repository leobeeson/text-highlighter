# Tech test

For your assignment we'd like you to read and understand the code for this small Python Web API, then do the tasks listed below.

What we will be looking for in your submission:
- Clean code, descriptive function and variable names, use of PEP 484 type hints where possible, well-structured code
- Comprehensive suite of unit tests for the entire submission
- Clear signs of use of TDD in your work. The best way to show this is by first writing test(s), committing them, then writing implementation that matches these tests. You can use rebase to clean up you commits before sending us the submission.
- All the unit tests must be passing

What we WON'T be looking for in your submission:
- Code written in the most optimal way possible - We don't think that LeetCode-style interviews represent a real-world working conditions]
- Finishing the test in a given amount of time. *This is not a race, so take as much time as you need.*

# Getting started

When you receive the code for this tech test, please make a new public repository on your personal Github account, and push it as is with a commit message "Initial commit.".

Next, create a feature branch (we'll leave the naming convention up to you). This is the branch we'd like you to add your changes to. Once you're done with the test, please raise a Pull Request from that branch to the main branch, but don't merge it.

When you're ready, simply send us the link to that repository through your recruiter.

*If you have ANY problems with running the project, please reach out to us through your recruiter, and we'll be happy to assist you.*

## Task 1

You're building an API endpoint `/message/highlight` that is supposed to highlight all provided words in a given text.
Imagine that your colleague started this project, but then was pulled off it to do something else more critical, and you're left with finishing it. Your imaginary colleague was kind enough to make a start on writing unit tests for the `src.text_processing.highlight_text()` function, but never got to implementing the `src.text_processing._highlight_words()` function.
The function should clean the text from any duplicated spaces, e.g. `Hello   world` becomes `Hello world`.
Your task is to implement it in a way that makes the existing tests pass

## Task 2

Turns out, the test suite in `tests.text_processing.test_highlight_text` is not as exhaustive as your imaginary colleague claimed.
Please add tests that should test other potential use-cases of the `highlight_text()` function.

## Task 3

To finish things off with that `highlight_text()` feature, please add a suite of tests for the FastAPI route `/message/highlight`.
Your imaginary colleague was kind enough to write one example test for it that tests the endpoint with an empty message.

# Task 4

Currently, this Web API is versioned as `0.1.0`. Please update the version of the API to `0.2.0`.

# Task 5

Your imaginary colleague tried to take a stab at implementing the `src/text_processing/remove_emojis` function, but after adding the test, the colleague realised that the implementation is broken.
Please fix the implementation so that all tests for that function pass.
