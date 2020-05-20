c = int(input())
lista = []
for i in range(c):
    pokemon = input()
    if pokemon not in lista:
        lista.append(pokemon)
resposta = 151 - len(lista)
print('Falta(m) {} pomekon(s).'.format(resposta))
