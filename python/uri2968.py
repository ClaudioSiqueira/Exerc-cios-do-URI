from math import ceil
voltas, placas = map(int, input().split(' '))
placa_total = voltas * placas
porcem = 10
cont = 0
while True:
    conta = ceil((placa_total * porcem) / 100)
    cont += 1
    porcem += 10
    if cont < 9:
        print('%s' % conta, end=' ')

    if cont == 9:
        print('%s' % conta)
        break