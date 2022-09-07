import pytest

from answer import generateParenthesis, isPalindrome

def test_generateParenthesis():
    assert generateParenthesis(0) == ['']
    assert generateParenthesis(1) == ['()']
    assert generateParenthesis(2) == ['(())', '()()']
    assert generateParenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
    
def test_isPalindrome():
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
