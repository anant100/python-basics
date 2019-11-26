
# To define your own iterators(loop) we need to use __iter__ & __next__ methods.
# Generator is also used to define the iterators but without using __iter__ & __next__ methods.

def topten():

    n = 1

    while n<=10:
        yield n
        n+=1


values = topten()

for i in values:
    print(i)

print("It's the same as for loop, but Generators are used when you only want to use the values one by one without storing it.")
