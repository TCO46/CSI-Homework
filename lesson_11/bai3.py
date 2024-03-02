# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

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


a = ['b', 'c', 'a', 'f', 'd', 'e']
print(quickSort(a))
