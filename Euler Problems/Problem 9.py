check = True
x1 = 0
x2 = 0
c = 0
for x in (range(1,1000)):
    if check:
        for y in (range(1,1000)):
            if x+y+(x**2+y**2)**0.5 == 1000:
                a = int(x)
                b = int(y)
                c = int((a**2+b**2)**0.5)
                print(a,b,c)
                check = False
                break
            else:
                continue
    else:
        break



print('The product of abc is: %s' %(a*b*c))