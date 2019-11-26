
# print only first number from List which is devisible by 5. If there is no number devisible by 5, then print "Not found" only once.

nums = [11,15,9,32,25]

for i in nums:
    if i % 5 == 0:
        print(i)
        break


else:
    print("Not found")