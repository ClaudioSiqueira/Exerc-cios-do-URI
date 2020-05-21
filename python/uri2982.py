quant = int(input())
verba = 0
gasto = 0
for i in range(quant):
    letra, dinherio = map(str, input().split(' '))
    dinherio = int(dinherio)
    if letra == 'G':
        gasto += dinherio
    else:
        verba += dinherio
total = verba - gasto
if total < 0:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
else:
    print('A greve vai parar.')