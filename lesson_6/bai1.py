def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


my_list = [4, 7, 2, 5]
bubble_sort(my_list)
print("Sorted array:", my_list)
