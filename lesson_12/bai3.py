def quick_sort(arr):
    # Nếu length của list <= 1 thì return lại list
    if len(arr) <= 1:
        return arr

    # lấy phần tử cuối trong list
    pivot = arr.pop()

    # 2 biến này để lưu các phần tử
    left = []
    right = []

    # tạo 1 vòng lặp cho list
    for i in arr:
        # nếu i <= pivot (phần tử cuối của list) thì cho vào biến left
        if i <= pivot:
            left.append(i)
            print("left: ", left)
            print("pivot 1: ", pivot)

        else:
            # còn lại thì cho vào biến right
            right.append(i)
            print("right: ", right)
            print("pivot 2: ", pivot)

    # trả về list đã được sắp xếp
    return quick_sort(left) + [pivot] + quick_sort(right)


a = [1, 5, 4, 12, 2, 45, 63, 102, 99, 87, 47, 65]
print("Step by Step of quick Sort")
print(quick_sort(a))
