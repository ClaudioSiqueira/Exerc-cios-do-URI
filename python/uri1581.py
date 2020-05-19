quant = int(input())
resposta = ''
for i in range(quant):
    lista = []
    c = int(input())
    for j in range(c):
        lista.append(input())
    primeiro = lista[0]
    for p in lista:
        if p == primeiro:
            resposta = lista[0]
        else:
            resposta = 'ingles'
            break
    print(resposta)
