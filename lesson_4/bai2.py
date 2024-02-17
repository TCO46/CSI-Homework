a = []
n = int(input("enter n: "))

for i in range(n):
    a.append(int(input()))


def find_num(arr, x):
    for index, i in enumerate(arr):
        if (i == x):
            return index + 1
    return -1


print(find_num(a, 5))
