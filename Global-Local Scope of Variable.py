

# Global variable - a

a = 10
def something():
    # Local variable - a
    a = 5
    print("In fun", a)


something()
print("Out fun", a)


# Add New line
print()


# Change the value of Global variable a from inside function
print("Change the value of Global variable a from inside function")
a = 10
def something():
    # calling global variable a
    global a
    a = 5
    print("In fun", a)


something()
print("Out fun", a)


# Add New line
print()


# Change the value of Global variable a from inside function without affecting the local variable a
print("Change the value of Global variable a from inside function without affecting the local variable a")
a = 10
def something():
    # calling global variable a & changing its value
    globals()['a'] = 15
    a = 5
    print("In fun", a)


something()
print("Out fun", a)
