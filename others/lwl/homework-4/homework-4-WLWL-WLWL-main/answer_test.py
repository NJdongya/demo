import pytest

from answer import unique_list, multiply, get_average 

def test_unique_list():
    assert unique_list([1,2,3,3,3,3,4,4,5]) == [1, 2, 3, 4, 5]
    
def test_multyply():
       assert multiply([9, 2, 3, -6, 7]) == -2268

def test_get_average():
    assert get_average(5,6,8,10,31) == 12

