
# Main Class
class Student:

    def __init__(self):
        self.name = input("Please Enter your name: ")
        self.roll_no = int(input("Please Enter your Roll Number: "))

        # Create object to use Inner Class
        self.lap = self.Laptop()

    def show(self):
        print("Name = {} & Roll number = {}".format(self.name, self.roll_no))
        # Call Object to print
        self.lap.show()

    # Inner Class
    class Laptop:

        def __init__(self):
            print("\nPlease Enter the detail about your Laptop")
            self.brand = input("Please Enter the Brand Name: ")
            self.RAM = input("What's the RAM of your laptop: ")

        def show(self):
            print("\nThis is information about {}'s laptop".format(s1.name))
            print("Laptop Brand = {} & RAM = {}".format(self.brand, self.RAM))


s1 = Student()
s1.show()


