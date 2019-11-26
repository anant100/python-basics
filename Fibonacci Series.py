

def fibo():
    a = 0
    b = 1
    lst = [a, b]
    n = int(input("First how many fibonacci series do you want: "))

    if n == 1:
        print([a])
    elif n < 1:
        print("Wrong Number.... Please enter valid number")
    else:
        # for i in range(2,n):
        for i in range(n-2):
            c = a + b
            lst.append(c)
            a, b = b, c
        print(lst)


fibo()
