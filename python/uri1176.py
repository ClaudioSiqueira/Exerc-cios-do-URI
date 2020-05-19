quantidade = int(input())
lista = [0, 1]
for j in range(0, quantidade):
    n = int(input())

    n1 = 0
    n2 = 1

    for i in range(0, 61):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        lista.append(n3)
    if n == 0:
        print('Fib(0) = 0')
    else:
        print('Fib({}) = {}'.format(n, lista[n]))
