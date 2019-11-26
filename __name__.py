
print("__name__ is used as the main file. If you want to make any file as a main file, use __name__")
print("Let's say you want to welcome user if when he comes first time to you.\n")


def welcome():
    print("Hello")
    print("Welcome user")


if __name__=="__main__":
    welcome()

print()
print()
print("Now if you will import this python file as a module to any other file and run it then you will not get the welcome in output")
