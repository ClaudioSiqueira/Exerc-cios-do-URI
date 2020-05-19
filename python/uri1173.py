N = int(input())
lista = []
for i in range(0, 10):
    lista.append(N)
    N *= 2
for j, v in enumerate(lista):
    print('N[{}] = {}'.format(j, v))
