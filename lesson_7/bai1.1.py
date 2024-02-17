def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i + 1

    return -1


a = [1, 5, 4, 7, 6]
print(search(a, 7))
