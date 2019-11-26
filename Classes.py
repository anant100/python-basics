# Define the class in CamelCase format
class Computer:

    # Define function in class (Ignore self for now)
    def config(self):
        print("i5, 16gb, 1TB")


# point an object to class behavior
comp1 = Computer()


# Call function with object
Computer.config(comp1)

# Another way to call function
print("\nBest way to call")
comp1.config()
