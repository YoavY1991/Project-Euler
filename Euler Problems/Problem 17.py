def lenginnum(s, e):
    '''Returns the number of letters needed to write all numbers in range.this function is
    limited up to 1000'''
    dic = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
           9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
           15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
           20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
           80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}

    string = []
    for x in range(s, e + 1):
        if len(str(x)) == 1:
            string.append(dic.get(x))
        elif 9 < x < 20:
            string.append(dic.get(x))
        elif len(str(x)) == 2 and int(str(x)[1]) == 0:
            string.append(dic.get(x))
        elif len(str(x)) == 2:
            string.append(str(dic.get(int(str(x)[0] + '0'))) + str(dic.get(int(str(x)[1]))))
        elif len(str(x)) == 3 and int(str(x)[1]) == 0 and int(str(x)[2]) == 0:
            string.append(str(dic.get(int(str(x)[0])) + 'hundred'))

        elif len(str(x)) == 3 and int(str(x)[1]) == 0 and int(str(x)[2]) != 0:
            string.append(
                str(dic.get(int(str(x)[0]))) + 'hundred' + 'and' + (dic.get(int(str(x)[2]))))

        elif len(str(x)) == 3 and int(str(x)[1]) == 1:
            string.append(str(dic.get(int(str(x)[0]))) + 'hundred' + 'and' + (
                dic.get(int(str(str(x)[1]) + (str(x)[2])))))

        elif len(str(x)) == 3 and int(str(x)[1]) != 0 and int(str(x)[2]) == 0:
            string.append(
                str(dic.get(int(str(x)[0])) + 'hundred' + 'and' + str(dic.get(int(str(x)[1:])))))
        elif len(str(x)) == 3 and int(str(x)[1]) != 0 and int(str(x)[2]) != 0:
            string.append(str(dic.get(int(str(x)[0])) + 'hundred' + 'and' + str(
                dic.get(int(str(x)[1] + '0'))) + str(dic.get(int(str(x)[2])))))
        elif len(str(x)) == 4 and int(str(x)[1]) == 0 and int(str(x)[2]) == 0 and int(
                str(x)[3]) == 0:
            string.append((str(dic.get(int(str(x)[0])) + (str(dic.get(x))))))
        else:
            string.append('notsupportednumber')

    sumis = 0
    for x in string:
        sumis += len(x)

    return sumis


print(lenginnum(1, 1000))