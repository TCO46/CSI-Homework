def insertionSort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = x


a = [1, 5, 4, 7, 6]
insertionSort(a)
print(a)
