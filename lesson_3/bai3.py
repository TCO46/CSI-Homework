def fibonacci_sum(n):
    if n <= 0:
        return 0

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    sum = 0
    for i in range(n):
        sum += fibonacci(i)
    return sum


print(fibonacci_sum(5))
