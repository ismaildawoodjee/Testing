# Testing

`requirements_dev.txt` contains packages for running tests.

## Directory Structure

Use `tree` with flag `-a` to print all files, `-I` to exclude some files, and
pipe the output to `clip.exe` to copy to clipboard.

Command to generate tree structure:

```bash
tree -a -I '<files_to_be_excluded>|<file2>|</file3>' | clip.exe
```

```bash
.
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
└── tests
    ├── __init__.py
    └── test_linked_list.py
```

## Running tests

For `mypy`:

```python
mypy src
```

For `flake8`:

```python
flake8 src
```

For `pytest`:

```python
pytest .
```

Generate `pytest` coverage report with:

```python
pytest --cov-report='html'
```
