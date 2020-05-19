N = int(input())
for i in range(0, N):
    cont = 0
    x = int(input())
    for j in range(1, x):
        if x % j == 0:
            cont += j
    if x == cont:
        print('{} eh perfeito'.format(x))

    else:
        print('{} nao eh perfeito'.format(x))

