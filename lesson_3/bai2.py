def exponential(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    return x * exponential(x, n-1)


print(exponential(2, 3))
