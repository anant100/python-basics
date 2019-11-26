
# # # #
# # # #
# # # #
# # # #
print("\np1 Pattern\n")


def p1():
    for i in range(4):
        for j in range(4):
            print ("# ",end="")
        print()


p1()

print("\np2 Pattern\n")


#
# #
# # #
# # # #
def p2():
    for i in range(4):
        for j in range(i+1):
            print ("# ",end="")
        print()


p2()

# # # #
# # #
# #
#
print("\np3 Pattern\n")


def p3():
    for i in range(4):
        for j in range(4-i):
            print ("# ",end="")
        print()


p3()
