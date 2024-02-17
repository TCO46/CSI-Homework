a = []
n = int(input("enter n: "))

for i in range(n):
    a.append(int(input()))


def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2

        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid + 1
    return -1


print(binary_search(a, 10))
