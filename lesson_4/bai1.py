a = [1, 3, 5, 7, 8, 9]

x = int(input("enter x: "))


def find_num(arr, x):
    for index, i in enumerate(arr):
        if (i == x):
            return index + 1
    return -1


print(find_num(a, x))
