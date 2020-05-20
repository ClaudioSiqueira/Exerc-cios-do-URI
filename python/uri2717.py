minutos = int(input())
a, b = map(int, input().split(' '))
if a + b <= minutos:
    print('Farei hoje!')
else:
    print('Deixa para amanha!')
