"""
Write a function, intersection, 
that takes in two lists, a,b, as arguments. 
The function should return a new list 
containing elements that are in both of the two lists.

You may assume that each input list 
does not contain duplicate elements.
"""


def intersection(a, b):
    # turn one list into a set to remove duplicates
    set_a = set(a)
    # iterate through the set and if a member is found in
    # the other set then add it to the result
    return [ item for item in b if item in set_a ]