c = int(input())
lista = []
comportou = n_comportou = 0
for i in range(c):
    nome = input()
    if nome[0] == '-':
        n_comportou += 1
    else:
        comportou += 1
    lista.append(nome[2:])
lista.sort()
for name in lista:
    print(name)
print('Se comportaram: %d | Nao se comportaram: %d' % (comportou, n_comportou))
