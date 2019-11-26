
import sys

# Recursion means the function calling itself. (Function inside the function)

# Be default limit in python is 1000.
print("Check Recursion limit in Python")
print(sys.getrecursionlimit())

# You can change the limit if you want
print("Change the Recursion limit in python")
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

# Example: Find factorial of a number using recursion
print()
print("Find the Factorial using Recursion Method")
n = int(input("For which number do you want to find the factorial: "))


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


result = fact(n)

print("Factorial of {} using Recursion is: ".format(n), result)

