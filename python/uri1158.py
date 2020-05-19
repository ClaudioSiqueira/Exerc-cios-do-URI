cont = 1
soma = 0
N = int(input())
for i in range(0, N):
    X, Y = input().split(' ')

    X = int(X)
    Y = int(Y)

    while True:

        if (X + cont) % 2 == 1:
            soma += (X + cont)
        cont += 1

        if cont == 2 * Y:

            cont = 0
            break
    print(soma)
    soma = 0