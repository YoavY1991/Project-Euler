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

sumis = 2
lista = [2]
for num in range(3,2000000,2):
    if isprime(num):
        sumis += num
        lista.append(num)
    else:
        continue

print(sumis)
print(lista)
print(sum(lista))

