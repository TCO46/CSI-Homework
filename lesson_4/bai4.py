a = []
n = int(input("enter n: "))

for i in range(n):
    a.append(int(input()))


def get_nearest_value(arr, x):
    temp = 0
    dist = abs(float(arr[0] - x))
    index = 0

    for i in range(len(arr)):
        temp = abs(float(arr[i] - x))

        if (dist > temp):
            dist = temp
            index = i

    return arr[index]


print(get_nearest_value(a, 10))
