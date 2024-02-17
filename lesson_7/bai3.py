def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def search(arr):
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] % 4 == 0:
            return i + 1

    return -1


a = [1, 5, 4, 7, 6]
bubble_sort(a)
print(search(a))
print(a)
