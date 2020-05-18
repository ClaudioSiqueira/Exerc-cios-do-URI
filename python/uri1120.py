lista = []
while True:
    a, b = map(str, input().split(' '))
    if a == '0' and b == '0':
        break
    for numero in b:
        if numero != a:
            lista.append(numero)
    try:
        while lista[0] == '0':
            del(lista[0])
    except IndexError:
        lista.append('0')
    for i in lista:
        print(i, end='')
    print()
    lista.clear()