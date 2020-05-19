while True:
    c = int(input())
    if c == 0:
        break
    else:
        planeta_menor = ''
        menor = 0
        for i in range(c):
            nome, ano, tempo = input().split()
            a = int(ano)
            t = int(tempo)
            conta = a - t
            if i == 0:
                menor = conta
                planeta_menor = nome
            else:
                if menor > conta:
                    menor = conta
                    planeta_menor = nome
        print(planeta_menor)
