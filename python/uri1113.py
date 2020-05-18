while True:
    X, Y = input().split(' ')

    X = int(X)
    Y = int(Y)

    if X < Y:
        print('Crescente')
    elif X > Y:
        print('Decrescente')
    else:
        break
