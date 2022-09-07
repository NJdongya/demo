import pytest

from answer import add_binary, plus_one, roman_to_integers

def test_both_empty():
    result = add_binary('', '')
    assert(result == None)

def test_first_empty():
    result = add_binary('', '1010')
    assert(result == None)

def test_second_empty():
    result = add_binary('1010', '')
    assert(result == None)

def test_first_nonbinary():
    result = add_binary('1301', '1010')
    assert(result == None)

def test_second_nonbinary():
    result = add_binary('1010', '1301')
    assert(result == None)

def test_example1():
    result = add_binary('11', '1')
    assert(result=="100")

def test_example2():
    result = add_binary('1010', '1011')
    assert(result=="10101")

def test_case_1():
    result = add_binary('10101111', '010101')
    assert(result=='11000100')

def test_case2():
    result = add_binary('111', '101')
    assert(result=='1100')
    


def test_example1():
    digits = [1, 2, 3]
    assert([1, 2, 4] == plus_one(digits))

def test_example2():
    digits = [1, 0, 9, 9]
    assert([1, 1, 0, 0] == plus_one(digits))

def test_case1():
    digits = [9, 9]
    assert([1, 0, 0] == plus_one(digits))

def test_case2():
    digits = [1, 9, 9]
    assert([2, 0, 0] == plus_one(digits))

def test_case3():
    digits = [9]
    assert([1, 0] == plus_one(digits))






def test_example1():
    roman_string = "III"
    assert(3 == roman_to_integers(roman_string))


def test_example2():
    roman_string = "IV"
    assert (4 == roman_to_integers(roman_string))


def test_example3():
    roman_string = "IX"
    assert (9 == roman_to_integers(roman_string))


def test_example4():
    roman_string = "LVIII"
    assert (58 == roman_to_integers(roman_string))


def test_example5():
    roman_string = "MCMXCIV"
    assert (1994 == roman_to_integers(roman_string))


def test_case1():
    roman_string = "XC"
    assert (90 == roman_to_integers(roman_string))


def test_case2():
    roman_string = "LXXX"
    assert (80 == roman_to_integers(roman_string))


def test_case3():
    roman_string = "LXXX"
    assert (80 == roman_to_integers(roman_string))


def test_case4():
    roman_string = "CXXXVII"
    assert (137 == roman_to_integers(roman_string))

