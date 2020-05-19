matriz = []
lugar = int(input())
operacao = str(input())
for i in range(12):
    matriz.append([])

for l in range(0, 12):
    for c in range(0, 12):
        n = float(input())
        matriz[l].append(n)
if operacao == 'S':
    soma = 0
    for k in range(0, 12):
        soma += matriz[k][lugar]
        print(soma)
if operacao == 'M':
    soma = 0
    for k in range(0, 12):
        soma += matriz[k][lugar]
    media = soma/12
    print('{:.1f}'.format(media))