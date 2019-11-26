
print("\n__init__ is called by default. You don't need to call it. It will automatically assigned to all objects of Class\n")

class Computer:

    def __init__(self):
       print("Init")

    def config(self):
        print("i5, 1TB")

com1 = Computer()
com2 = Computer()

com1.config()
com2.config()

# Define variables in init
print("\n Define Variables in __init__\n")
class Computer1:

    def __init__(self, cpu, RAM):
       self.cpu = cpu
       self.RAM = RAM

    def config(self):
        print("Config is:", self.cpu, self.RAM)

com1 = Computer1('i3', 16)
com2 = Computer1('AMD', 8)

com1.config()
com2.config()


# Extra to learn how to compare (AND OR) update the values
print("\n\n Extra (Update & Compare value)\n")
class Computer2:

    def __init__(self):
       self.cpu = 'name'
       self.RAM = 6

    def config(self):
        print("Config is:", self.cpu, self.RAM)

    def compare(self, com2):
        if com1 == com2:
            print("same")
        else:
            print("diff")


com1 = Computer2()
com2 = Computer2()

com1.cpu = 'new'
com2.RAM = 9

com1.compare(com2)

com1.config()
com2.config()
