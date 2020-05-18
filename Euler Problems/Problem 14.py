def collatz(n):
    chain = [n]
    while chain[-1] > 1:
        if chain[-1] % 2 == 0:
            chain.append(int(chain[-1] / 2))
        else:
            chain.append(int(chain[-1] * 3 + 1))
    return chain


def colletz_longest_chain(s):
    a = s
    starting = 0
    length = 0

    while a > 1:
        if len(collatz(a)) > length:
            length = len(collatz(a))
            starting = a
            a -= 1
        else:
            a -= 1
    return print(f"Longest chain for collatz series in range provided  - \nStaring number: {starting}\nlength {length}")


colletz_longest_chain(1000000)