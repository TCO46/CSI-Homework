def sum_of_number(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_number(n - 1)


print(sum_of_number(3))
