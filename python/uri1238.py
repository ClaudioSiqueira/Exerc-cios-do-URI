loop = int(input())
for w in range(0, loop):
    a, b = str(input()).split(' ')
    menor = a
    maior = b
    cont2 = 0
    final = ''
    if len(b) < len(a):
        menor = b
        maior = a

    lista_a = []
    lista_b = []
    lista_ab = []
    lista_maior = 0
    cont = 0
    for i in a:
        lista_a.append(i)
    for j in b:
        lista_b.append(j)
    for c in range(0, len(menor)):
        lista_ab.append(lista_a[cont] + lista_b[cont])
        cont += 1

    for l in lista_ab:
        print(l, end='')
    if len(a) != len(b):
        print(maior[len(menor) - len(maior):], end='')
    print('')