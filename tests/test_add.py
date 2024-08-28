import pytest
from source.add_string_number import add


def test_add ():
    result = add("1")
    assert result == 1
