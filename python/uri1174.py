lista = []
for i in range(0, 100):
    x = float(input())
    lista.append(x)
for j, v in enumerate(lista):
    if v <= 10:
        print('A[{}] = {}'.format(j, v))
