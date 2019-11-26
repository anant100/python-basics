# Operator overloading is used to overload with the by default operator methods.
# In this program, there is some mistakes in operations assignment but the logic you can understand how to work.


class Student:

    def __init__(self):
        self.marks1 = 60
        self.marks2 = 80

    # Operator Overloading Method
    def __add__(self, other):
        total = self.marks1 + self.marks2
        return total

    def __str__(self):
        return "{}".format(self.marks1)


s1 = Student()
s2 = Student()

# '+' operator only add values from same data types (Int, Float, String, etc)
s1.t1 = s1.marks1 + s1.marks2
print("Total Marks by adding int:", s1.t1)

# Here '+' is calling by-default method named '__add__' in the background & it can not add two objects. So, we need to overload the operator by defining method.
t2 = s1 + s2

# Let's print values for s1 & s2 first.
# It will not print value, it will only print type & address. So we need to overload method named '__str__'
print("Print Object values:", s1)

# Now print the total
print("Total marks by adding 2 objects: ", t2)
