"""
Python Functions and Recursions
"""
"""
QUESTION 1: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
["((()))","(()())","(())()","()(())","()()()"]
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
"""
def generateParenthesis(n):
    def backtrack(ans, curr, openp, closep, maxp):
        if len(curr) == 2 * maxp:
            ans.append(curr)
        if openp < maxp:
            backtrack(ans, curr + '(', openp + 1, closep, maxp)
        if closep < openp:
            backtrack(ans, curr + ')', openp, closep + 1, maxp)

    ans = []
    openp, closep = 0, 0
    curr = ''
    backtrack(ans, curr, openp, closep, n)
    return ans
"""
QUESTION 2: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
=========================================
Input: "race a car"
Output: false
Write a function named isPalindrome that takes a string as an input and returns a bool as an output.
"""
def isPalindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        a, b = s[i].lower(), s[j].lower()
        if a.isalnum() and b.isalnum():
            if a != b:
                return False
            else:
                i, j = i + 1, j - 1
                continue
        i, j = i + (not a.isalnum()), j - (not b.isalnum())
    return True
