import pytest
from source.add_string_number import add

''' handle empty'''
def test_add_handle_empty ():
    result = add("")
    assert result == 0

'''handle single value'''
def test_add_handle_single():
    result = add("4")
    assert result == 4

'''handle multiple value'''
def test_handle_two_values() : 
    result = add("1,5")
    assert  result == 6 