hora_inicial, minuto_inicial, hora_final, minuto_final = input().split(' ')

hora_inicial = int(hora_inicial)
hora_final = int(hora_final)
minuto_inicial = int(minuto_inicial)
minuto_final = int(minuto_final)

hora_total = hora_final - hora_inicial

if hora_total < 0:
    hora_total += 24

minuto_total = minuto_final - minuto_inicial

if minuto_total < 0:
    minuto_total += 60
    hora_total -= 1

if minuto_total == 0 and hora_total == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora_total, minuto_total))
