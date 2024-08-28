import pytest
from source.add_string_number import add


def test_add ():
    result = add("1,5")
    assert result == 6
