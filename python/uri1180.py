N = int(input())
menor = 0
indice = 0
X = list(map(int, input().split()))
for i, v in enumerate(X):
    if i == 1:
        menor = v
        indice = i
    else:
        if v < menor:
            menor = v
            indice = i
print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(indice))

