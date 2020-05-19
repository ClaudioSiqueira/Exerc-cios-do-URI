quantidade = int(input())
cont = 0
if quantidade != 1:
    while True:
        print('Ho ', end='')
        cont += 1
        if cont == quantidade - 1:
            break
    print('Ho!')
else:
    print('Ho!')