# Testing

[![Tests](https://github.com/ismaildawoodjee/Testing/actions/workflows/workflow.yml/badge.svg)](https://github.com/ismaildawoodjee/Testing/actions/workflows/workflow.yml)
[![Codecov](https://codecov.io/gh/ismaildawoodjee/Testing/branch/main/graph/badge.svg?token=KYUUMHRLGC)](https://codecov.io/gh/ismaildawoodjee/Testing)

`requirements_dev.txt` contains packages for running tests.

## Directory Structure

Use `tree` with flag `-a` to print all files, `-I` to exclude some files, and
pipe the output to `clip.exe` to copy to clipboard.

Command to generate tree structure:

```bash
tree -a -I '<files_to_be_excluded>|.git|.venv|<more_files_or_folders>' | clip.exe
```

```bash
.
├── .github
│   └── workflows
│       └── tests.yml
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
├── requirements_dev.txt
├── setup.cfg
├── setup.py
├── src
│   └── data_structures
│       ├── __init__.py
│       └── linked_list.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_linked_list.py
│   └── test_linked_list_node.py
└── tox.ini
```

## Running tests

For `mypy`, testing only the `src` directory:

```python
mypy src
```

For `flake8`, to test both the `src` and `tests` directory:

```python
flake8 src tests
```

For `pytest`:

```python
pytest
```

Generate `pytest` coverage report with:

```python
pytest --cov-report='html'
```

## Static Type Checking

MyPy is a static type checker, to check if variable types are what you expect them to be.

MyPy's `is None` type guard, to check if something is `None` or not:

```python
def func(val: Optional[str]):
    """Example for `is None` type guard."""
    if val is not None:
        # explicitly use `val is not None`, not just `val`
        # Here, type of val is narrowed to str
        print(val)
    else:
        # can optionally skip else
        # Type of val is now narrowed to None
        pass
```
