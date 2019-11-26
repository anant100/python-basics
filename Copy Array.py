
# from numpy import *
import numpy

arr1 = numpy.array([1, 2, 3, 4, 5])
arr2 = arr1

print("\nArray 1: ", arr1)
print("Array 2: ", arr2)

# Here we've successfully capied array but the location for both array is still same.
print("Location of Array 1: ", id(arr1))
print("Location of Array 2: ", id(arr2))

# Types of Copy
# Shallow Copy - It make copy from array and also change the location.

print("\n------- Shallow Copy -----------")
arr1 = numpy.array([1, 2, 3])
arr2 = arr1.view()
print("\nArray 1: ", arr1)
print("Array 2: ", arr2)
print("Location of Array 1: ", id(arr1))
print("Location of Array 2: ", id(arr2))

# Now if we will change the value of any element from array 1, it will automatically reflect to array 2.
arr1[2] = 5
print("\nChanged Array 1: ", arr1)
print("Changed Array 2: ", arr2)
print("Location of Array 1: ", id(arr1))
print("Location of Array 2: ", id(arr2))

# Deep Copy - It make copy from array and also change the location and also differenciate the arrays if any value is changed after.

print("\n------- Deep Copy -----------")
arr1 = numpy.array([1, 2, 3])
arr2 = arr1.copy()
print("\nArray 1: ", arr1)
print("Array 2: ", arr2)
print("Location of Array 1: ", id(arr1))
print("Location of Array 2: ", id(arr2))

# Now if we will change the value of any element from array 1, it will automatically reflect to array 2.
arr1[2] = 5
print("\nChanged Array 1: ", arr1)
print("Changed Array 2: ", arr2)
print("Location of Array 1: ", id(arr1))
print("Location of Array 2: ", id(arr2))
