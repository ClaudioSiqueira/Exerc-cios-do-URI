contar = 0
lista = []
for i in range(1, 22):
    lista.append(i)

for j in range(1, 21):
    n = int(input())
    lista[j] = n
for c in lista[::-1]:
    print('N[{}] = {}'.format(contar, c))
    contar += 1
    if contar == 20:
        break

