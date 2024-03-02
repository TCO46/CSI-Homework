def selection_sort(arr):
    for i in range(len(arr)):

        min = i

        for j in range(i + 1, len(arr)):

            if (arr[min] > arr[j]):
                min = j

        if (min != i):
            arr[i], arr[min] = arr[min], arr[i]


a = [5, 3, 8, 4, 2]
selection_sort(a)
print(a)
