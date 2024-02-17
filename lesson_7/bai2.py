def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if (arr[min] > arr[j]):
                min = j
        if (min != i):
            arr[i], arr[min] = arr[min], arr[i]


def binary_search(arr):
    selection_sort(a)
    # arr = [num for num in arr if num % 2 == 0]
    smallest = arr[0]

    for i in arr:
        # print(i)
        if i < smallest:
            print(i)
            smallest = i

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < smallest:
            left = mid + 1
        elif arr[mid] > smallest:
            right = mid - 1
        else:
            return mid + 1
    return -1


a = [6, 5, 1, 3, 10]

print(binary_search(a))
