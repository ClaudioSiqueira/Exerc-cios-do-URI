lista = []
cont = 0
for i in range(0, 6):
    a = float(input())
    if a > 0:
        cont += 1
        lista.append(a)
media = sum(lista)/len(lista)
print('{} valores positivos'.format(cont))
print('{:.1f}'.format(media))
