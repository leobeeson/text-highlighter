# Project Management Notes

## Business Logic Requirements

### `/message/highlight`
* Endpoint `/highlight` highlights all provided words in a given text.
* Endpoint `/highlight` removes banned emojis in a given text.


### Doubts:
* What could go wrong with the `/message/highlight` enpoint?
    * What kind of mistakes might the user/client do interacting with the endpoint?
        * **Send a `list` instead of a `string` as message argument.**
        * **Send an empty `list` instead of an empty `string` as message argument.**
        * **Send a blacklist `string` instead of a `list`.**
    * What scenarios could cause the arguments passed by the user/client to make the endpoint fail? 
        * **Send blacklist argument not _lower-cased_.** #DONE
        * **Send n-grams (where n > 1) as blacklist terms.** #DONE
        * **Text with multiple spaces between words AND an actual blacklist.** #DONE
    * What kind of errors can we foresee?


***


## WBS:
* Implement `src/text_processing/highlight_text.py._highlight_words()` function. #TODO_1#DONE
* Make all existing tests for `src.text_processing.highlight_text()` pass. #TODO_1#DONE
* Add tests to `tests/text_processing/test_highlight_text.py` that test other potential use-cases of the `highlight_text()` function. #TODO_2#DONE
    * Enforce lower-casing of blacklist items. #DONE
    * Handle n-grams (where n > 1) as blacklist terms. #DONE
    * Replicate test_text_with_multiple_spaces() but with an actual blacklist. #DONE
        * The `src.text_processing._highlight_words()` function cleans the text from any duplicated spaces, e.g. `Hello   world` becomes `Hello world`. #DONE
* Add a suite of tests for the FastAPI route `/message/highlight`. #TODO_3#DONE
    * Add integration tests to `tests/routes/message/test_highlight_message.py`. #DONE
        * Input validation tests:
            * Message: #DONE
                * Field missing #DONE
                * Wrong type -> send `list[str]` #DONE
            * Recipient: #DONE
                * Field missing #DONE
            * Sender: #DONE
                * Field missing #DONE
            * Timestamp: #DONE
                * Field missing #DONE
                * Is iso? #DONE
            * Blacklist:
                * Field missing #DONE
                * Wrong type:
                    * Integer #DONE
                    * Float #DONE
    * Add http exception/error-catching tests. #DONE
* Update the version of the API to `0.2.0`. #TODO_4
    * The `tests/routes/test_status.py` gets the `version` variable from `src/version.py`.
    * However, `src/routes/status.py` has the version number hard-coded.
        * Remove duplication by pointing `src/routes/status.py` to the `version` variable from `src/version.py` (single point of change).
* Fix the implementation of `src/text_processing/remove_emojis` so that all tests for that function pass. #TODO_5
    * `tests/text_processing/test_remove_emojis.py` has only one test with parameterised arguments (3x). 
        * Shall we add some more texts? #DOUBT#TODO_5


***


# Developer Notes

## Creating the Virtual Environment

### direnv
* The shell command `direnv allow` doesn't execute in WSL2 (Ubuntu 20.04). Instead, run the following from bash terminal (not zsh): 
    ```bash
    eval "$(direnv hook bash)"
    ```
* You'll now see the expected shell output:
    ```bash
    direnv: loading ~/projects/ds-tech-interview/.envrc
    direnv: export +VIRTUAL_ENV ~PATH
    ```

### .envrc
* The `.envrc` file defines the python version at a mayor level, i.e.: 
    ```bash
    python3
    ```
* If in your local machine the alias `python3` points to a Python version < 3.9, you need to change the Python version ponting to the alias python3 to on >=3.9.  
* To make sure you create a virtual environment a Python version > 3.9, follow the next steps:  

1. Check the different Python 3.* versions on your local machine:
    ```bash
    ls /usr/bin/python3*
    ```

2. If you have a Python version > 3.9, execute the next step, if not, first install the latest Python version available:
    ```bash
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
    ```
    * Notice the command above is defining Python3.10 as the version for the Python3 alias. Make sure to change this to whatever major.minor version you've installed.

