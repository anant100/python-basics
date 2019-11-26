

num = int(input("\nPlease enter the number to check whether it's Prime number or not: "))

for i in range(2, num):
    if num % i == 0:
        print(num, " is not Prime number")
        break
else:
    print(num, " is Prime Number")
