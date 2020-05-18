def allfactors(n):
    global factors
    import math
    factors = []
    for x in range(1, int(math.sqrt(n)) + 1):
        if n % x == 0:
            factors.append(x)
            factors.append(int(n / x))


def isprime(n):
    allfactors(n)
    return len(factors) == 2


def maxprime(n):
    maxprime = 0
    allfactors(n)
    for y in factors:
        if isprime(y) and y > maxprime:
            maxprime = y
        else:
            continue
    return maxprime


max = maxprime(600851475143)

print(max)