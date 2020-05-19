from math import hypot
cont = 0
lista = ''
lista2 = []
while True:
    lista = input().split(' ')
    if lista[0] == '0':
        break
    for i in lista:
        lista2.append(int(i))
    cont += 1
    if hypot(lista2[1], lista2[2]) <= lista2[0] * 2:
        print('Pizza %i fits on the table.' % cont)
    else:
        print('Pizza %i does not fit on the table.' % cont)
    lista = ''
    lista2.clear()