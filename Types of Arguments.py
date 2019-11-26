
# Types of arguments:
# - Position Arguments
# - Keyword Arguments
# - Default Arguments
# - Variable Length Arguments


def person(name, age):
    print(name)
    print(age)

# Position Arguments
person('Anant', 23)

# Add New line
print()

# Keyword Arguments
person(age=22, name='Anant')

# Add New line
print()

# Default Arguments
def person(name, age=18):
    print(name)
    print(age)

person('Anant')

# Add New line
print()

# Variable Length Arguments (When you are not sure how many arguments user can pass)


def add(a, *b):
    # Here a is int & b wil be stored as tuple, So we can't make sum like (a+b)
    c = a
    for i in b:
        s = c + i

    print(s)


print("Addition is: ")
add(3, 4, 2)
