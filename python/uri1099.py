cont = 0
N = int(input())
for i in range(0, N):
    X, Y = input().split(' ')

    X = int(X)
    Y = int(Y)

    if Y > X:
        for j in range(X + 1, Y):
            if j % 2 == 1:
                cont += j
        print(cont)
        cont = 0
    elif X > Y:
        for j in range(Y + 1, X):
            if j % 2 == 1:
                cont += j
        print(cont)
        cont = 0
    else:
        print(0)
