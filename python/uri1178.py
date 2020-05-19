n = float(input())
cont = 0
while True:
    print('N[{}] = {:.4f}'.format(cont, n))
    n /= 2
    cont += 1
    if cont == 100:
        break
