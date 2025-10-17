import math

def pair_product(numbers, target_product):
  dicty = {}

  # enumerate with index and value
  for idx, num in enumerate(numbers):
    # find the coefficient but dont store it because it might be a float
    coeff = target_product / num

    # if it already exists in the dictionary then 
    # we have our pair
    if coeff in dicty:
      return (dicty[coeff], idx)

    # if not then just store the numbers and their indices as you iterate
    # to especially avoid float problem
    dicty[num] = idx
    