numbers = list(map(int, input().split(',')))
oddNumbers = numbers[:]
evenNumbers = numbers[:]
dividedByFour = numbers[:]
primeNumbers = numbers[:]


def Average(lst):
    return int(sum(lst) / len(lst))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


for numbers in evenNumbers:
    if (numbers % 2 != 0):
        evenNumbers.remove(numbers)
for numbers in evenNumbers:
    if (numbers % 2 == 0):
        oddNumbers.remove(numbers)
for numbers in dividedByFour:
    if (numbers % 4 != 0):
        dividedByFour.remove(numbers)
for numbers in primeNumbers:
    if (is_prime(numbers) == False):
        primeNumbers.remove(numbers)


print(Average(oddNumbers), Average(evenNumbers),
      Average(dividedByFour), Average(primeNumbers))

print(f"""
    Trung bình số lẻ: {Average(oddNumbers)}
    Trung bình sô chẵn: {Average(evenNumbers)}
    Trung bình số chia cho 4: {Average(dividedByFour)}
    Trung bình số nguyên: {Average(primeNumbers)}
    Tổng số lẻ: {sum(oddNumbers)}
    Tổng số chẵn: {sum(evenNumbers)}
    Tổng số chia cho 4: {sum(dividedByFour)}
    Tổng số nguyên: {sum(primeNumbers)}
    """)
