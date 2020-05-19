quantidade = int(input())
for q in range(0, quantidade):
    lista = []
    numero = ''
    ponto = 0
    final = 1
    n = str(input())
    for i in n:
        if i != '!':
            lista.append(i)
        else:
            ponto += 1
    for j in lista:
        numero += j
    numero = int(numero)

    for c in range(numero, 1, -ponto):
        final *= c
    print(final)