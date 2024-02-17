a = []
n = int(input("enter n: "))

for i in range(n):
    a.append(int(input()))


def max(arr):
    max = arr[0]
    for i in range(len(arr)):
        if (arr[i] > max):
            max = arr[i]

    return max


def min(arr):
    min = arr[0]
    for i in range(len(arr)):
        if (arr[i] < min):
            min = arr[i]

    return min


print(max(a))
