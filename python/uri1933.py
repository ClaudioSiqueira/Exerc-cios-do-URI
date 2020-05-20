c1, c2 = str(input()).split(' ')
c1 = int(c1)
c2 = int(c2)
lista = [c1, c2]
if c1 == c2:
    print(c1)
else:
    print(max(lista))
