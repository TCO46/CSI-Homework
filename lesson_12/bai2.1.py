def linear_search(arr, x):
    # Tạo vòng lặp với biên i từ 0 -> lenght của list 
    for i in range(len(arr)):
        # Nếu giá trị arr[i] bằng x (giá trị cần tìm) thì trả về vị trí của 
        if arr[i] == x:
            return i + 1
    # nếu không thì trả về 
    return -1
-1

a = [1, 5, 4, 87, 4, 6, 10, 54, 21, 16, 42, 32]
print(linear_search(a, 16))
