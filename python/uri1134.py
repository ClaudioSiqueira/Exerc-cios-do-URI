alcool = 0
gasolina = 0
disel = 0
x = 0
while x != 4:
    x = int(input())
    if x == 1:
        alcool += 1
    elif x == 2:
        gasolina += 1
    elif x == 3:
        disel += 1
    elif x == 4:
        break
print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(disel))
