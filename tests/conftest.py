"""Config file for Pytest - it has to be exactly named `conftest.py`"""
import pytest
import sys


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def write_to_buffer(statement):
        buffer["stdout"] += statement
        buffer["write_calls"] += 1

    # monkeypatch changes the `write` attribute of `sys.stdout` to `write_to_buffer`
    # and returns the `sys.stdout`'s functionality back to original after the test is done
    monkeypatch.setattr(sys.stdout, "write", write_to_buffer)
    return buffer
