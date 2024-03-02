def bubble_sort(arr):
    # cho n là length của list
    n = len(arr)

    # tạo vòng lặp cho arr vớii biến i
    for i in range(n):
        # tạo vòng lặp cho arr với biến j từ 0 -> n-i-1 (VD: 0 -> 12-1-1 = 10)
        for j in range(0, n-i-1):
            # nếu arr[j] < arr[j+1] thì hoán đổi 2 giá trị lại với nhau
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


my_list = [1, 5, 4, 12, 2, 45, 63, 102, 99, 87, 47, 65]
bubble_sort(my_list)
print("Sorted array:", my_list)
