salario = float(input())
if salario <= 400:
    ajuste = salario + (salario * 0.15)
    pcem = 15
elif 400 < salario <= 800:
    ajuste = salario + (salario * 0.12)
    pcem = 12
elif 800 < salario <= 1200:
    ajuste = salario + (salario * 0.10)
    pcem = 10
elif 1200 < salario <= 2000:
    ajuste = salario + (salario * 0.07)
    pcem = 7
else:
    ajuste = salario + (salario * 0.04)
    pcem = 4
print('Novo salario: {:.2f}'.format(ajuste))
print('Reajuste ganho: {:.2f}'.format(ajuste - salario))
print('Em percentual: {} %'.format(pcem))

