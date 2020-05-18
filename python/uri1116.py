N = int(input())
for i in range(0, N):
    X, Y = input().split(' ')

    X = int(X)
    Y = int(Y)

    if Y == 0:
        print('divisao impossivel')
    else:
        divisao = X/Y
        print(divisao)
