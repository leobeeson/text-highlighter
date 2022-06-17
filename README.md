# Data Science Tech Interview repository

## Pre-requisites

- Python 3.9+
- [Direnv](https://direnv.net/)


## Creating a virtual environment using venv

In order for the project to run, you'll need to configure a virtual environment.
This process is automated thanks to the [Direnv](https://direnv.net/).
The only thing you have to do to create an environment is to run the following in the root of your project:

```shell
direnv allow
```

Expected output:
```shell
direnv: loading ~/projects/ds-tech-interview/.envrc
direnv: export +VIRTUAL_ENV ~PATH
```


## Installing dependencies

Once the virtual environment is ready, you'll have to install all requirements:

```shell
pip install -r requirements.txt
```


## Running the app

To start the app, simply run the following in the root of this project:

```shell
python -m src
```


## Testing

To start the tests, simply run the following in the root of this project:

```shell
pytest
```

The tests can also be run in a continuous mode:

```shell
ptw
```

# Interview tasks

Once you have the project working, please open the [TASKS.md](TASKS.md) file to see what you have to do as part of your interview.
