def print_numbers(n):
    if n < 0:
        return 0
    else:
        print_numbers(n - 1)
        print(n)


print_numbers(10)
