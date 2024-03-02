# hàm sắp xếp sử dụng bubble sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def binary_search(arr, x):
    # Goi hàm sắp xếp 
    bubble_sort(arr)
    print(arr)
    
    # Gọi 2 biến left và right 
    left = 0
    right = len(arr) - 1
    
    # khi left <= right thì vòng lặp tiếp diễn 
    while left <= right:
        # Tính mid = cách lấy left + right và chia hết cho 2
        mid = (left + right) // 2
        
        # nếu giá trị arr[mid] < x thì cho left = mid + 1
        if arr[mid] < x:
            left = mid + 1
        # nếu arr[mid] > x thì cho right = mid - 1 
        elif arr[mid] > x:
            right = mid - 1
        # còn lại thì giá trị đó nằm ở mid + 1
        else:
            return mid + 1
    # nếu không tìm được thì trả về -1
    return -1


a = [1, 5, 4, 87, 4, 6, 10, 54, 21, 16, 42, 32]
print(binary_search(a, 16))
