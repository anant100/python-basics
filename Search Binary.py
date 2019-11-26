# Binary Search requires Sorted List
pos = -1


def search(list, n):

    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


list1 = [4, 6, 3, 1, 9, 0, 79, 89, 56, 894]

# Binary Search requires Sorted List
list = sorted(list1)
print("Sorted List is :", list)
n = 1

if search(list, n):
    print("Found at ", pos+1)
else:
    print("Not Found")
