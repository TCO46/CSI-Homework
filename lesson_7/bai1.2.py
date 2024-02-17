def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        print("min = ", min)
        for j in range(i + 1, len(arr)):
            print(arr[min], arr[j])
            if (arr[min] > arr[j]):
                min = j
                print("min = ", min, "j = ", j)
        if (min != i):
            arr[i], arr[min] = arr[min], arr[i]
            print(arr)
    # print(arr)


def binary_search(arr, x):
    selection_sort(arr)

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


a = [1, 5, 4, 7, 6]
selection_sort(a)
# print(binary_search(a, 7))
