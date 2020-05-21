total = int(input())
loop = int(input())
lista = []
for i in range(loop):
    figurinha = int(input())
    if figurinha not in lista:
        lista.append(figurinha)
print(total - len(lista))
