n = 40
d = range(2,21)
length = len(d)
current = 0

def check(a):
    global current
    for denominator in d:
        if a % denominator == 0:
            current+=1
        else:
            current = 0
            break

while current < 19:
    check(n)
    if current < 19:
        n+=20

print(n)

