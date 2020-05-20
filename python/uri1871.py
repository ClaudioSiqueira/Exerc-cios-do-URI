while True:
    a, b = map(int, input().split(' '))
    if a == 0 and b == 0:
        break
    else:
        final = ''
        soma = str(a + b)
        for letra in soma:
            if letra != '0':
                final += letra
        print(final)
