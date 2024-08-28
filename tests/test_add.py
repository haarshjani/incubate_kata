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


'''handle n number to add'''

def test_handle_n_number ():
    result = add("1,2,3,4")
    assert result == 10

'''handle new lines'''
def test_handle_newline():
    result = add("1\n,2,3")
    assert result == 6

'''handle dynamic deliminator'''
def test_handle_dynamic_deliminator():
    result = add("//;\n1;2")
    assert result == 3