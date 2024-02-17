a = []
n = int(input("enter n: "))

for i in range(n):
    a.append(int(input()))


def find_sum(arr, x):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j] == x):
                return i + 1, j + 1

    return -1


print(find_sum(a, 10))
