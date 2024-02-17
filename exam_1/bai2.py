def gcd(a, b, i=1, res=0):
    if i > a and i > b:
        return res

    if a % i == 0 and b % i == 0:
        res = i

    return gcd(a, b, i + 1, res)


print(gcd(8, 100))
