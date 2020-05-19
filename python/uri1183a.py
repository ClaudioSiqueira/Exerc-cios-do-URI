operacao = str(input())
matriz = []

for i in range(12):
    for j in range(12):
        numero = float(input())
        if i < j:
            matriz.append(numero)

if operacao == 'S':
    print(("%.1f")%(sum(matriz)))
else:
    print(("%.1f")%(sum(matriz)/len(matriz)))
