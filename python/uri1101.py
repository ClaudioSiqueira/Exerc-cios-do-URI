cont = 0
while True:
    M, N = input().split(' ')

    M = int(M)
    N = int(N)

    if M <= 0:
        break
    if N <= 0:
        break

    if N > M:
        for i in range(M, N + 1):
            cont += i
            print(i, end=' ')
        print('Sum={}'.format(cont))
        cont = 0

    elif M > N:
        for i in range(N, M + 1):
            cont += i
            print(i, end=' ')
        print('Sum={}'.format(cont))
        cont = 0
