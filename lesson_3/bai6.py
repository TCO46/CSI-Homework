# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_array = [0, 1]
#         for i in range(2, n):
#             fib_array.append(fib_array[i-1] + fib_array[i-2])
#         return fib_array

def fibonacci(n, current=0, next=1, count=0):
    if n <= 0:
        return 0
    elif count < n:
        print(current)
        return fibonacci(n, next, current + next, count + 1)
    else:
        return ""


fibonacci(5)
