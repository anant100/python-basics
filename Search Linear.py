
pos = -1


def search(list, n):
    for i in range(len(list)):
        globals()['pos'] = i
        if list[i] == n:
            return True
    return False


list = [4, 6, 3, 1, 9, 0]

n = 1

if search(list, n):
    print("Found at ", pos+1)
else:
    print("Not Found")
