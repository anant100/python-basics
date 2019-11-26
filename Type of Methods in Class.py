# Types of Methods:
# - Instance Methods - It's used for Instance variables.
# - Class Methods - It's used for Class variables
# - Static Methods - It's used when you don't want to use Class OR Instance variable & you want to use any other instance variables


class Student:

    # Class Variable
    school = 'MCIT'

    # Instance Method
    def __init__(self, m1, m2, m3):
        # Instance Variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # Class Method
    @classmethod
    def get_school(cls):
        return cls.school

    # Static Method
    @staticmethod
    def info():
        print("This is static Method. You can use any operation without using Class OR Instance variables.")


s1 = Student(10,30,40)
s2 = Student(20,30,40)

print("School name is: ", Student.get_school())

print("Avg for Student 1: ", s1.avg())
print("Avg for Student 2: ", s2.avg())
print()
Student.info()
