 #!/usr/bin/python
"""
Python  Functions
"""

# Write a function unique_list() that takes a list and returns a new list with unique elements of the first list.
# unique_list: (1,2,3,3,3,3,4,4,5)

def unique_list(lst):
    lst = list(lst)
    new_lst = list(set(lst))
    new_lst.sort(key=lst.index)
    return new_lst

#Write a function multiply() to multiply all giving numbers in a list.
#Sample List : (9, 2, 3, -6, 7)
#Expected Output : -2268

def multiply(lst):
    lst = list(lst)
    res = 1
    for x in lst:
        res = res * x
    return res


# Write a function get_average() that takes an arbitrary number of arguments and returns the average of them
# Number of arguments : (5,6,8,10,31)
# Expected Output : 12

def get_average(*lst):
    lst = list(lst)
    return sum(lst)/len(lst)
