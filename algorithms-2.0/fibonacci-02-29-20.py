"""
  implement function that will return the ith position in the fibonacci sequence
    * starts with 1
    * handle < 1 input
  implement it in different ways:
    1. recursively
    2. with some dynamic programming (memoization)
    3. iteratively
"""

# recursive naive solution
def fibonacci(index):
  if index == 0:
    print('no thanks')
  elif index == 1 or index == 2:
    return 1
  else:
    return fibonacci(index - 1) + fibonacci(index - 2)

# with cache
def fibonacci(index, cache={}):
  if index == 0:
    print('no thanks')
  elif index == 1 or index == 2:
    return 1
  elif cache.get(index):
    return cache[index]
  else:
    cache[index] = fibonacci(index - 1, cache) + fibonacci(index - 2, cache)
    return cache[index]


# iterative solution
def fibonacci(index):
  sequence =  []

  for i in range (index):
    if i == 0 or i == 1:
      sequence.append(1)
    else:
      sequence.append( sequence[i - 1] + (sequence[i - 2]))
  return sequence[index - 1]

if __name__ == '__main__':
  expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
 987, 1597, 2584, 4181, 6765]
  # result = [ fibonacci(i) for i in range(1, 5 + 1) ]
  # uncomment this one after memoized solution is done
  result = [ fibonacci(i) for i in range(1, 100) ]
  print('results     : ', result)
  # print('20 expected : ', expected)
