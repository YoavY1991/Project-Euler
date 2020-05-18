primes = [2]
c = 3
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


while len(primes) < 10001:
    if isprime(c):
        primes.append(c)
        c+=2
    else:
        c+=2

print(len(primes))
print(primes[-1])
print(primes)