inicial, final = input().split(' ')
inicial = int(inicial)
final = int(final)

tempo = final - inicial
if inicial > final:
    tempo = (final + 24) - inicial
elif final == inicial:
    tempo = 24
print('O JOGO DUROU {} HORA(S)'.format(tempo))