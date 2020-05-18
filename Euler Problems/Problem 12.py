# This function returns the number for which is the "n" triangular number - for example:
#  [n=1,0+1 = 1] [n=2, 1+2=3] [n=3, 1+2+3 = 6]

def triangular(n):
    return int((n * (n + 1)) / 2)

# This function supposed to find the first triangular number that may be divided mor than 500 numbers

from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

def tdividedby(x):
    import math
    a = 1
    while len(factors(triangular(a))) < x:
        a += 1

    print('number %s is the %s t number and can be divided by %s numbers' %(triangular(a), a, len(factors(triangular(a)))))


tdividedby(500)