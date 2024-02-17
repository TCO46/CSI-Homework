def sum_of_divisors(n, i=1, divisors_sum=0):
    if i > n:
        return divisors_sum
    if n % i == 0:
        divisors_sum += i
    return sum_of_divisors(n, i + 1, divisors_sum)


print(sum_of_divisors(6))
