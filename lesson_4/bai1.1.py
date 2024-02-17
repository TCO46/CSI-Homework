a = [1, 3, 5, 7, 8, 9]

x = int(input("enter x: "))


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


print(binary_search(a, x))
