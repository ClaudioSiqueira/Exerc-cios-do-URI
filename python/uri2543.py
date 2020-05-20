while True:
    try:
        c, idi = map(int, input().split(' '))
        cont = 0
        for i in range(c):
            autor, jogo = map(int, input().split(' '))
            if autor == idi and jogo == 0:
                cont += 1
        print(cont)
    except EOFError:
        break
