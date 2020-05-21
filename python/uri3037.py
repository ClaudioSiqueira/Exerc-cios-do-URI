quant = int(input())
for c in range(quant):
    cont = 0
    maria_pont = 0
    maria_dist = 0
    joao_pont = 0
    joao_dist = 0
    for i in range(6):
        cont += 1
        pontuacao, distancia  = map(int, input().split(' '))
        if cont <= 3:
            joao_pont += pontuacao
            joao_dist += distancia
        else:
            maria_pont += pontuacao
            maria_dist += distancia
    if joao_dist * joao_pont > maria_dist * maria_pont:
        print('JOAO')
    else:
        print('MARIA')