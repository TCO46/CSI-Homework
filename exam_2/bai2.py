def search_smallest(arr):
    smallest = arr[0]

    for i in arr:
        if i < smallest:
            smallest = i

    return smallest


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def reverse_bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def binary_search_largest(arr):
    bubble_sort(arr)
    largest = arr[0]

    for i in arr:
        if i > largest:
            largest = i

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < largest:
            left = mid + 1
        elif arr[mid] > largest:
            right = mid - 1
        else:
            return mid + 1
    return -1


a = [4, 12, 5, 8, 70, 6]
print("Mang goc: ", a)
print("So lon nhat: ", binary_search_largest(a))
print("So be nhat: ", search_smallest(a))

print("Mang da sap xep: ", bubble_sort(a))


def findKLargest(arr, k):
    reverse_bubble_sort(arr)

    return arr[:k][-1]


k = 3
print(f"So lon thu {k} la: {findKLargest(a, k)}")


b = [4, 12, 5, 8, 70, 6]


def insertX(arr, x, pos):
    pos -= 1
    return [* arr[:pos], x, *arr[pos:]]


print(f"Mang da chen so 66 vao vi tri thu 4 la: {insertX(b, 66, 4)}")
