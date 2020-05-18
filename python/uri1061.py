dia_inicial = int(input().split()[1])
hora = input().split(':')
hora_inicial = int(hora[0])
minuto_inicial = int(hora[1])
segundo_inicial = int(hora[2])

dia_final = int(input().split()[1])
hora = input().split(':')
hora_final = int(hora[0])
minuto_final = int(hora[1])
segundo_final = int(hora[2])

dia = dia_final - dia_inicial

hora = hora_final - hora_inicial
if hora < 0:
    hora += 24
    dia -= 1

minuto = minuto_final - minuto_inicial
if minuto < 0:
    minuto += 60
    hora -= 1

segundo = segundo_final - segundo_inicial
if segundo < 0:
    segundo += 60
    minuto -= 1

print('{} dia(s)'.format(dia))
print('{} hora(s)'.format(hora))
print('{} minuto(s)'.format(minuto))
print('{} segundo(s)'.format(segundo))
