a = [1, 2, 5, 7, 15, 22, 41, 55, 65, 74, 82, 91]


def find_x(x, arr):
    for index, i in enumerate(arr):
        if (i == x):
            return index
    return -1


print(find_x(74, a))


def find_x_binary(x, arr):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2

        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid
    return -1


print(find_x_binary(74, a))
