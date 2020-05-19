lista = []
for i in range(0, 10):
    x = int(input())
    if x <= 0:
        x = 1
    lista.append(x)
for i, v in enumerate(lista):
    print('X[{}] = {}'.format(i, v))
