from argsets import __version__
from argsets.argsets import hello  # this means, in argsets/argsets.py, import the function, hello
import pytest

def test_version():
    assert __version__ == '0.1.0'

def  test_world():
    assert hello() == "world"
