

import array

val = array.array('i', [3, 4, 5, -1, 6, 9])
print("\n", val)

# Reverse Array
val.reverse()
print("\nReverse Array: ", val)

# Print values one by one
print("\nValues printed one by one\n")
for i in range(len(val)):
    print(val[i])

# Another way to Print values one by one
print("\nAnother way Values printed one by one\n")
for i in val:
    print(i)

# Copy array to new array
print("\n Copy array values with square of it to new array\n")
new = array.array(val.typecode, [a*a for a in val])
print(new)
