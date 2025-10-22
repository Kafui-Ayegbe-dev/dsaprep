"""
Write a function, allUnique,
 that takes in an array. The function should
 return a boolean indicating whether or not
 the array contains unique items.
"""

def allUnique(a):
    return len(set(a)) == len(a)