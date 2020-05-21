quant = int(input())
boneca = carro = 0
for i in range(quant):
    string = str(input())
    if string[-1] == 'F':
        boneca += 1
    else:
        carro += 1
print('{} carrinhos'.format(carro))
print('{} bonecas'.format(boneca))
