quant = int(input())
frase = list(input().split(' '))
lista = []
for num in frase:
    lista.append(int(num))
cont = 0
resposta = 0
maior = lista[0]
for n in lista:
    cont += 1
    if n >= maior:
        maior = n
    else:
        resposta = cont
        break
print(resposta)
