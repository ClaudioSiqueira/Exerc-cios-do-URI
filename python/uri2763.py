cpf = input()
formatado = ''
for numero in cpf:
    if numero.isnumeric():
        formatado += numero
    else:
        numero = ' '
        formatado += numero
for i in formatado.split(' '):
    print(i)
