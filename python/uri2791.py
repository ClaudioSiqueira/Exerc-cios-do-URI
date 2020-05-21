a, b, c, d = map(int, input().split())
lista = [a, b, c, d]
for i, v in enumerate(lista):
    if v == 1:
        print(i + 1)