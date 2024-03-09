def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()

    left = []
    right = []

    for i in arr:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quickSort(left) + [pivot] + quickSort(right)


def binary_sort(arr, x):
    arr = quickSort(arr)

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid + 1
    return -1


def delete_odd(arr):
    new_list_of_even = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            new_list_of_even.append(arr[i])

    return new_list_of_even


def add_number(arr, num):
    arr.append(num)
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = x


a = [1, 5, 13, 15, 20, 2]
# uncomment tung cai de test
# find_number = int(input("Enter the number you need to find: "))
# print(binary_sort(a, find_number))

# print(delete_odd(a))

# number = int(input("Enter you number: "))
# add_number(a, number)
# print(a)
