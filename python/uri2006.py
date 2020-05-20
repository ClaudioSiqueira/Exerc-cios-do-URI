cha = str(input())
cont = 0
a, b, c, d, e = str(input()).split(' ')
lista = [a, b, c, d, e]
for i in lista:
    if i == cha:
        cont += 1
print(cont)
