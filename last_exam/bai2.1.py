def fibonacci(n):
    if n <= 1:
        return n
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))