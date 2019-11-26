
# Idea is to get the list of numbers from the user and return the number of even numbers and odd numbers.


n = int(input("Please enter how many numbers which you want to enter: "))
lst = []

for i in range(n):
    num = int(input("Number: "))
    lst.append(num)

print("Your list is: ", lst)


# Now counting the evens & odds


def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1

    print("Even: ", even)
    print("Odd: ", odd)

    # Another format to print with values
    print("Even: {} & Odd: {}".format(even, odd))


count(lst)
