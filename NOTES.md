



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

