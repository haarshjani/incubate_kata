import pytest
from source.add_string_number import add


def test_add ():
    result = add("")
    assert result == 0
