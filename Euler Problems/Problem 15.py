#x = cubes on x line y = cubes o n y
x = 3
y = 1


#Number of nods\intersections
inter =  (x+1)*(y+1)

#List of all nods
ilist = list(range(1,inter+1))

#Creating lists of rightest row and bottom row in order to map the connections correctly
last_on_right = [x for x in range(x+1,inter+1,x+1)]
last_on_bottom = [x for x in range(((x+1)*y+1),(inter+1))]

#This will be the list containing nested lists mapping the connection between the nodes. So the first [i0] of every list is the nod itself, and the following numbers are the nods to which i0 can go to.
moves_options = []
moves_options_2 = []

#The following loop creating the moves_options list
for i,n in enumerate(ilist):
    if n not in last_on_right and n not in last_on_bottom:
        moves_options.append([n,ilist[i+1],ilist[i+(x+1)]])
        moves_options_2.append([n,ilist[i+1],ilist[i+(x+1)]])
    elif n in last_on_right and n not in last_on_bottom:
        moves_options.append([n,ilist[i+(x+1)]])
        moves_options_2.append([n,ilist[i+(x+1)]])
    elif n in last_on_bottom and n not in last_on_right:
        moves_options.append([n,ilist[i+1]])
        moves_options_2.append([n,ilist[i+1]])
    else:
        moves_options.append([n])
        moves_options_2.append([n])

del moves_options_2[0][1]
print(moves_options)
print(moves_options_2)

routes = []
while True:
    try:
        if len(moves_options[0]) == 2:
            moves_options = moves_options_2
        nod = 0
        dot = 0
        route = [1]
        root = []
        print(moves_options)
        while True:
            nod = moves_options[nod][1] - 1
            if len(moves_options[nod]) > 1:
                route.append(moves_options[nod][0])
                dot = 1
            else:
                dot = 0
                route.append(moves_options[nod][0])
                break

        routes.append(route)

        a = -2
        while True:
            if len(moves_options[route[a] - 1]) > 2:
                del moves_options[route[a] - 1][1]
                break
            else:
                a -= 1

        print(moves_options)
    except:
        break

