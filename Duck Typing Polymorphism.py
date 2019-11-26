
# Duck typing Polymorphism - This is used when only the behaviour matters to you not the name of class.


class Pycharm:

    # Method name shoud be same in both class
    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:

    # Method name shoud be same in both class
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()

# You can change the class name anytime if the method name is same & it will change the output.
ide = Pycharm()
# ide = MyEditor()

lap = Laptop()
lap.code(ide)
