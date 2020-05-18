def func(n):
    sumis = 0
    string = (str(2**n))
    for x in string:
        sumis += int(x)
    return sumis

func(1000)