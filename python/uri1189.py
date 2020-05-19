operacao = str(input())
soma = 0
cont = 0
for linha in range(12):
    for coluna in range(12):
        n = float(input())
        if linha > coluna and (linha + coluna) < 11:
            soma += n
            cont += 1
if operacao == 'S':
    print('%.1f' % soma)
else:
    media = soma/cont
    print('%.1f' % media)