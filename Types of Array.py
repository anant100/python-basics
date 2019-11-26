
# from numpy import *
import numpy

# Simple Array
print("\nSimple Array\n")
arr = numpy.array([1, 2, 3, 4, 2, 3, 6, 7])
print(arr)

# Linspace Array (First, Last, No of parts) by default 50 parts
print("\nLinspace Array\n")
arr = numpy.linspace(1, 12, 12)
print(arr)

# Arange Array (Start, End, Steps)
print("\nArange Array\n")
arr = numpy.arange(1, 12, 2)
print(arr)

# logspace Array (Start, End, Parts) (10^start, 10^end, difference = 10^parts)
print("\nlogspace Array\n")
arr = numpy.logspace(1,50, 5)
print(arr)

# Print the original values by putting value of 'e'
for i in range(5):
    print("\n Value: "'%.2f' %arr[i])

# Zeros Array
print("\nZeros Array\n")
arr = numpy.zeros(5)
print(arr)

# Ones Array
print("\nOnes Array in int format\n")
arr = numpy.ones(5, int)
print(arr)

