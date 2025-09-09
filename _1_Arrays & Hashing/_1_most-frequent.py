# problem : most frequent char

def most_frequent_char(s):
  mydic = {}

  for char in s:
    if char not in mydic:
      mydic[char] = 1
    else:
      mydic[char] += 1

  res = ''
  highest = -99999
  
  for key in mydic:
    if mydic[key] > highest:
      highest = mydic[key]
      res = key

  return res