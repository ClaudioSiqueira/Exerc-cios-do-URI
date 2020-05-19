quantidade_test = int(input())
for j in range(0, quantidade_test):
    a, b = input().split(' ')

    if len(b) > len(a):
        print('nao encaixa')
    else:
        lista = []
        cont = 0
        final = ''
        tamanho = len(b)
        for i, v in enumerate(a):
            cont += 1
            if cont >= len(a) - len(b) + 1:
                lista.append(v)

        for c in lista:
            final += c
        if final == b:
            print('encaixa')
        else:
            print('nao encaixa')
