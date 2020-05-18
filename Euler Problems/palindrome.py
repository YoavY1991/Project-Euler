
def palindrome():
    a = list(range(100, 1000))[::-1]
    b = list(range(100, 1000))[::-1]
    list2 = [0]

    for x in a:
        for y in b:
            if str(x * y) == str(x * y)[::-1]:
                list2.append( x *y)
    return print(max(list2))


palindrome()