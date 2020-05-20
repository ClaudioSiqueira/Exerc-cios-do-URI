while True:
    try:
        linha, coluna = map(int, input().split(' '))
        matriz = []
        adjacente = 0
        for c in range(linha):
            a = list(map(int, input().split(' ')))
            matriz.append(a)
        for l in range(linha):
            for c in range(coluna):
                if matriz[l][c] == 1:
                    matriz[l][c] = 9

        for i in range(linha):
            for j in range(coluna):
                if matriz[i][j] == 0:
                    if j - 1 > -1:
                        if matriz[i][j - 1] == 9:
                            adjacente += 1
                    if j + 1 < coluna:
                        if matriz[i][j + 1] == 9:
                            adjacente += 1
                    if i + 1 < linha:
                        if matriz[i + 1][j] == 9:
                            adjacente += 1
                    if i - 1 > -1:
                        if matriz[i - 1][j] == 9:
                            adjacente += 1
                    matriz[i][j] = adjacente
                    adjacente = 0
        for l in range(linha):
            for c in range(coluna):
                print(matriz[l][c], end='')
            print()
    except EOFError:
        break
