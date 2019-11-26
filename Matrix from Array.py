
# ------------------ Error in Matrix ---------------------

# import numpy
from numpy import *

# 2-D Array
arr1 = array([
            [1, 2, 3],
            [6, 4, 5],
            [1, 6, 7]
])
# Convert 2-D array to Matrix
# m = matrix(arr1)
m = arr1
print(m)
# n = matrix('1 2 4; 2 5 4')
n = array([
            [1, 2, 3],
            [6, 8, 5],
            [2, 6, 7]
])

s = m + n
print("Sum:\n", s)

mul = m * n
print("Multiplication:\n", mul)

# Print Diagonal, min, max values of matrix
print("\nDiagonal of Matrix m")
print(m.diagonal())

print("\nMin of Matrix m")
print(m.min())

print("\nMax of Matrix m")
print(m.max())
