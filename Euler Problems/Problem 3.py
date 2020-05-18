nt = 371
check = True
while check:
    for number in reversed(list(range(3, int(nt / 3 + 1), 2))):
        if check == False:
            break
        else:
            if nt % number == 0:
                for x in range(3, int(number / 2 + 2), 2):
                    if number % x == 0:
                        break
                    elif x == list(range(3, int(number / 2 + 2), 2))[-1]:
                        print(number)
                        check = False
                        break
                    else:
                        continue
            else:
                pass

