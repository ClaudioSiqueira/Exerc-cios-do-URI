while True:
    mary = john = 0
    quant = int(input())
    if quant == 0:
        break
    string = str(input())
    for i in string:
        if i == '0':
            mary += 1
        elif i == '1':
            john += 1
    print('Mary won {} times and John won {} times'.format(mary, john))