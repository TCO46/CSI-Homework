def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if (arr[min] > arr[j]):
                min = j
        if (min != i):
            arr[i], arr[min] = arr[min], arr[i]


a = [1, 5, 4, 7, 6]
selection_sort(a)

print(a)
