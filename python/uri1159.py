cont = 0
soma = 0
while True:
    X = int(input())
    for i in range(0, 10):
        if (X + i) % 2 ==0:
            soma += X + i
    if X != 0:
        print(soma)

    if X == 0:
        break
    soma = 0