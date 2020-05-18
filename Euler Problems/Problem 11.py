a1 = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'
a2 = '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'
a3 = '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'
a4 = '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'
a5 = '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'
a6 = '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'
a7 = '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'
a8 = '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'
a9 = '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'
a10 = '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'
a11 = '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'
a12 = '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'
a13 = '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'
a14 = '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'
a15 = '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'
a16 = '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'
a17 = '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'
a18 = '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'
a19 = '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'
a20 = '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

l1 = [int(x) for x in a1.split()]
l2 = [int(x) for x in a2.split()]
l3 = [int(x) for x in a3.split()]
l4 = [int(x) for x in a4.split()]
l5 = [int(x) for x in a5.split()]
l6 = [int(x) for x in a6.split()]
l7 = [int(x) for x in a7.split()]
l8 = [int(x) for x in a8.split()]
l9 = [int(x) for x in a9.split()]
l10 = [int(x) for x in a10.split()]
l11 = [int(x) for x in a11.split()]
l12 = [int(x) for x in a12.split()]
l13 = [int(x) for x in a13.split()]
l14 = [int(x) for x in a14.split()]
l15 = [int(x) for x in a15.split()]
l16 = [int(x) for x in a16.split()]
l17 = [int(x) for x in a17.split()]
l18 = [int(x) for x in a18.split()]
l19 = [int(x) for x in a19.split()]
l20 = [int(x) for x in a20.split()]

allrows = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20]

sumof = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0

for l in allrows:
    for i,a in enumerate(l):
        if i < 17:
            if a*l[i+1]*l[i+2]*l[i+3] > sumof:
                sumof = a*l[i+1]*l[i+2]*l[i+3]
                n1 = a
                n2 = l[i+1]
                n3 = l[i+2]
                n4 = l[i+3]
            else:
                continue
        else:
            break

print(n1,n2,n3,n4,sumof)

columns = []
h = 0
while h < 20:
    for i,l in enumerate(allrows):
        columns.append(l[h])
    h+=1


c1 = [x for x in columns[0:20]]
c2 = [x for x in columns[20:40]]
c3 = [x for x in columns[40:60]]
c4 = [x for x in columns[60:80]]
c5 = [x for x in columns[80:100]]
c6 = [x for x in columns[100:120]]
c7 = [x for x in columns[120:140]]
c8 =  [x for x in columns[140:160]]
c9 =  [x for x in columns[160:180]]
c10 = [x for x in columns[180:200]]
c11 = [x for x in columns[200:220]]
c12 = [x for x in columns[220:240]]
c13 = [x for x in columns[240:260]]
c14 = [x for x in columns[260:280]]
c15 = [x for x in columns[280:300]]
c16 = [x for x in columns[300:320]]
c17 = [x for x in columns[320:340]]
c18 = [x for x in columns[340:360]]
c19 = [x for x in columns[360:380]]
c20 = [x for x in columns[380:400]]

allc = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20]

for l in allc:
    for i,a in enumerate(l):
        if i < 17:
            if a*l[i+1]*l[i+2]*l[i+3] > sumof:
                sumof = a*l[i+1]*l[i+2]*l[i+3]
                n1 = a
                n2 = l[i+1]
                n3 = l[i+2]
                n4 = l[i+3]
            else:
                continue
        else:
            break


print(n1,n2,n3,n4,sumof)



import numpy as np

x,y = 20,20

npa = np.asarray(allrows, dtype=np)

a = np.arange(x*y).reshape(x,y)

diags = [npa[::-1,:].diagonal(i) for i in range(-npa.shape[0]+1,a.shape[1])]

diags.extend(npa.diagonal(i) for i in range(npa.shape[1]-1,npa.shape[0],-1))


diagonals_left_up_right_down = list(([n.tolist() for n in diags]))


x,y = 20,20

npa1 = np.asarray((list(reversed(allc))), dtype=np)

b = np.arange(x*y).reshape(x,y)

diags2 = [npa1[::-1,:].diagonal(i) for i in range(-npa1.shape[0]+1,b.shape[1])]

diags2.extend(npa1.diagonal(i) for i in range(npa1.shape[1]-1,npa1.shape[0],-1))


diagonals_right_up_to_leftdown = list(([n.tolist() for n in diags2]))


for l in diagonals_right_up_to_leftdown[3:36]:
    for i,a in enumerate(l):
        if i <= (len(l)-4):
            if a*l[i+1]*l[i+2]*l[i+3] > sumof:
                    sumof = a*l[i+1]*l[i+2]*l[i+3]
                    n1 = a
                    n2 = l[i+1]
                    n3 = l[i+2]
                    n4 = l[i+3]
            else:
                continue
        else:
            break


print(n1,n2,n3,n4,sumof)

for l in diagonals_left_up_right_down[3:36]:
    for i,a in enumerate(l):
        if i <= (len(l)-4):
            if a*l[i+1]*l[i+2]*l[i+3] > sumof:
                    sumof = a*l[i+1]*l[i+2]*l[i+3]
                    n1 = a
                    n2 = l[i+1]
                    n3 = l[i+2]
                    n4 = l[i+3]
            else:
                continue
        else:
            break


print(n1,n2,n3,n4,sumof)

print('The largest multiple is  %s' %sumof)