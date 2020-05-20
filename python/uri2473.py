flavinho = list(map(int, input().split(' ')))
sorteio = list(map(int, input().split(' ')))
cont = 0
for i in flavinho:
    if i in sorteio:
        cont += 1
if cont == 3:
    print('terno')
elif cont == 4:
    print('quadra')
elif cont == 5:
    print('quina')
elif cont == 6:
    print('sena')
else:
    print('azar')
