# To use the Reduce method we need to import it.
from functools import reduce

# Lambda (Anonymous) function used when you want to define function without name.

f = lambda a : a*a
result = f(5)
print(result)

# Industrial Use: Get bunch of data & Filter it, perform some operation on it and reduce it.
# - Filter()
# - Map()
# - Reduce()

# Bunch of data
nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Filter it by finding Even numbers
evens = list(filter(lambda n : n%2==0, nums))
print(evens)

# Perform operation and find doubles of it
doubles = list(map(lambda n : n*2, evens))
print(doubles)

# Reduce is by making sum of all number from list (Reduce Method is imported from functool)
sum = reduce(lambda a,b : a+b, doubles)
print(sum)
