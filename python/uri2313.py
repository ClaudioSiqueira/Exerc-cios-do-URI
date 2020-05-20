a, b, c = map(int, input().split(' '))
lista = [a, b, c]
lista.sort()
tipo = ''
retangulo = ''
if a >= b + c or b >= a + c or c >= a + b:
    valido = 'Invalido'
    print(valido)
else:
    valido = 'Valido'
    if a == b == c:
        tipo = '-Equilatero'
    elif a != b != c != a:
        tipo = '-Escaleno'
    else:
        tipo = '-Isoceles'
    if lista[2] ** 2 == (lista[0] ** 2) + (lista[1] ** 2):
        retangulo = 'Retangulo: S'
    else:
        retangulo = 'Retangulo: N'
    print('{}{}'.format(valido, tipo))
    print('{}'.format(retangulo))
