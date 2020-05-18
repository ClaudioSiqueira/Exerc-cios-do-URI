while True:
    n1 = float(input())
    while n1 < 0 or n1 > 10:
        print('nota invalida')
        n1 = float(input())
    n2 = float(input())
    while n2 < 0 or n2 > 10:
        print('nota invalida')
        n2 = float(input())
    print('media = {:.2f}'.format((n1+n2)/2))
    X = int(input('novo calculo (1-sim 2-nao)\n'))
    while X > 2 or X < 1:
        X = int(input('novo calculo (1-sim 2-nao)\n'))
    if X == 2:
        break

