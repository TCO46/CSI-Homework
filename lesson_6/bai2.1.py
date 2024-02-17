def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i + 1

    return -1


a = [0, 9, 1, 5]
print(search(a, 9))
