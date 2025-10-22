"""
Write a function, exclusiveItems,
that takes in two arrays, a,b, 
as arguments. The function should 
return a new array containing elements 
that are in either array but not both arrays.
"""

def exclusive_items(a,b):
    set_a = set(a)
    set_b = set(b)

    res = []

    for val in set_a:
        if val not in set_b:
            res.append(val)

    for val in set_b:
        if val not in set_a:
            res.append(val)

    return res



def exclusive_items_also(a,b):
    # using the symmetric difference operator
    return list(set(a) ^ set(b))