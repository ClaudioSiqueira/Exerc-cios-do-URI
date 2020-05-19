operacao = str(input())
soma = 0
cont = 0
for linha in range(12):
    for coluna in range(12):
        n = float(input())
        if coluna > linha and (linha + coluna) >= 12:
            soma += n
            cont += 1
if operacao == 'S':
    print('%.1f' % soma)
else:
    media = soma/cont
    print('%.1f' % media)
