# problem: Write a function, pair_sum, that takes in a list and a target sum as arguments.
# The function should return a tuple containing a pair of indices whose elements sum to
# the given target. The indices returned must be unique.


def pair_sum(numbers, target_sum):

  dicty = {}

  for i in range(len(numbers)):

    diff = target_sum - numbers[i]
    # if the difference doesnt exist in the dictionary as in 
    # the other name that makes up the pair_sum
    # the store potential first half in the dictionary with its 
    # index as value
    if diff not in dicty:
      dicty[numbers[i]] = i
      # if the diff exists in the dicty
      # then it means we have found second half of the pair as numbers[i]
      # so return the tuple
    else:
      return (dicty[diff], i)
    