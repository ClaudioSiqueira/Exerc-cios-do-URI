lista = []
a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)


lista.append(a)
lista.append(b)
lista.append(c)
lista.sort()

print(lista[0])
print(lista[1])
print(lista[2])
print('')
print(a)
print(b)
print(c)
