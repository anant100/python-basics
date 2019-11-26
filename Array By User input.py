

import array

arr = array.array('i', [])

n = int(input("Enter the number of values in Array"))

for i in range(n):
    x = int(input("Please enter the value"))
    arr.append(x)

print(arr)

# Search the index number of the value in array

val = int(input("Please enter the value to search"))


for e in arr:
    if e == val:
        print("\nThe Index number of the value is: ", arr.index(e))
        break

