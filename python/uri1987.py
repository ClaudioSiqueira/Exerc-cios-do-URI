while True:
    try:
        cont = 0
        a, b = input().split(' ')
        for letra in b:
            cont += int(letra)
        if cont % 3 == 0:
            print('%d sim' % cont)
        else:
            print('%d nao' % cont)
    except EOFError:
        break
