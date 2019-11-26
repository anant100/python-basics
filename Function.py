
# Define function we use 'def function_name():'
def fun():
    x = 4
    print("Normal Value:", x)


fun()

# Functional arguments
def update(x):
    x = 8
    print("Functional Value:", x)


x = 10
print("Outer Functional Value:", x)
update(x)

# There is NO PassByValue & PassByReference concept in Python
def pas(lst):
    print()
    print(id(lst))

    lst[1] = 25
    print(id(lst))
    print("x ", lst)


print()
lst = [10, 20, 30]
print(id(lst))
print("lst ", lst)

pas(lst)
print("New lst after calling function:", lst)
