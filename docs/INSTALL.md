# Install the QHBM Library

There are three ways to start developing with the QHBM Library:
* Choose any example notebook at TODO, make a copy, and modify to suit your needs.
* Install the package in a local environment.
* Work from the source code.

## Pip package

### Requirements

## Install from source

### 1. Fork and clone the repository

In the top right of the GitHub project, under your profile picture, there is a button labelled "Fork". Click this button. You now have a personal repository with a copy of the library code.

Open a terminal. From your working directory, clone your forked copy of the library:
```
git clone https://github.com/USERNAME/qhbm-library.git
cd qhbm-library
```

Now you need to tell your local git client about the parent repo of your fork:
```
git remote add upstream https://github.com/google/qhbm-library.git
```

### 2. Install dependency manager

We use a Python dependency manager called [poetry](https://python-poetry.org/). Install it from source:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
```
After installation, follow the on screen instructions to ensure the `poetry` command can be found by your shell. Restart the shell and confirm successful installation:
```
poetry --version
```

### 3. Install QHBM Library

Poetry automatically manages your environment using the specifications in the `pyproject.toml` file. To initiate your `poetry` managed virtual environment and install all dependencies, simply run:
```
poetry install
```
To confirm that the QHBM Library has been successfully installed from source, you can run the unit tests:
```
poetry run pytest
```
