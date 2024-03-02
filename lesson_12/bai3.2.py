def insertionSort(arr):
    # tạo vòng lặp với biến i với khoảng 1 -> length củaa list
    for i in range(1, len(arr)):
        # cho biến x là 1 giá trị của list
        x = arr[i]
        print("x: ", x)
        # cho biến j là i - 1
        j = i - 1
        print("i: ", i)
        print("j: ", j)

        # khi j >= 0 và giá trị của arr[j] > x và x là arr[i] thì lặp vô tận
        while j >= 0 and arr[j] > x:
            # khi vòng lặp còn tiếp thì arr[j + 1] sẽ bằng arr[j]
            arr[j + 1] = arr[j]
            print("list condition 1: ", arr)
            # rồi j giảm đi 1
            j -= 1

        # hết vòng lặp thì sẽ thay giá trị arr[j + 1] sẽ là x l arr[i]
        arr[j + 1] = x
        print("list condition 2: ", arr)


a = [1, 5, 4, 12, 2, 45, 63, 102, 99, 87, 47, 65]
insertionSort(a)
print(a)
