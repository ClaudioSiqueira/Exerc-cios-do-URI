c = int(input())
for i in range(c):
    nome = ''
    x, y = map(int, input().split(' '))
    rafael = (3 * x) ** 2 + (y ** 2)
    beto = (2 * (x ** 2) + (5 * y) ** 2)
    carlos = (-100 * x) + (y ** 3)
    if rafael > beto and rafael > carlos:
        nome = 'Rafael'
    if beto > rafael and beto > carlos:
        nome = 'Beto'
    if carlos > beto and carlos > rafael:
        nome = 'Carlos'
    print('%s ganhou' % nome)