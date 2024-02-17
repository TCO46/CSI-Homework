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


a = [5, 3, 8, 4, 2]
print(quickSort(a))
