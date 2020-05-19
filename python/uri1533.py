while True:
    cont = 0
    c = int(input())
    if c == 0:
        break
    suspeitos = list(map(int, input().split(' ')))
    indice = suspeitos[:]
    suspeitos.sort()
    del(suspeitos[-1])
    resposta = max(suspeitos)
    for i, v in enumerate(indice):
        if v == resposta:
            print(i + 1)
            break
    del suspeitos
