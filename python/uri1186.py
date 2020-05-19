operacao = str(input())
soma = 0
cont = 0

for linha in range(12):
    for coluna in range(12):
        valor = float(input())
        if (coluna + linha) >= 12:
            soma += valor
            cont += 1
if operacao == 'S':
    print('%.1f' % soma)
else:
    print('%.1f' % (soma/cont))