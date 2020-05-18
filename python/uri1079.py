N = int(input())
lista = []
for i in range(0, N):
    a, b, c = input().split(' ')

    a = float(a)
    b = float(b)
    c = float(c)

    media = (a * 2 + b * 3 + c * 5)/ 10
    lista.append(media)
for indice, valor in enumerate(lista):
    print('{:.1f}'.format(valor))
