
import numpy

# 2-D Array
arr1 = numpy.array([
                    [1, 2, 3, 4, 5, 6],
                    [4, 5, 6, 4, 5, 6]
                    ])
print("2-D Aray: \n", arr1)
print("Type of Array:", arr1.dtype)
print("Dimensions of Array:", arr1.ndim)
print("Shape of Array: (rows, columns)", arr1.shape)
print("Size of Array: (rows*columns)", arr1.size)

# Multi-Dimension to Single Dimension Array
print("\nConvert Multi-Dimension to Single Dimension Array")
arr2 = arr1.flatten()
print(arr2)

# Single-Dimension to Multi-Dimension Array
print("\nConvert Single-Dimension to 2-Dimension Array")
arr3 = arr2.reshape(4, 3)
print(arr3)

print("\nConvert Single-Dimension to 3-Dimension Array")
arr4 = arr2.reshape(2, 2, 3)
print(arr4)
