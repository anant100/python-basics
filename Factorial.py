

n = int(input("For which number do you want to find the factorial"))


def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result*i

    print("Factorial of {} is: ".format(n), result)


fact(n)
