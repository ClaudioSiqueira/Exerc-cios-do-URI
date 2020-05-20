c = int(input())
for i in range(c):
    bonus = int(input())
    a1, d1, lv1 = map(int, input().split(' '))
    if lv1 % 2 == 0:
        golpeA = ((a1 + d1) / 2) + bonus
    else:
        golpeA = ((a1 + d1) / 2)

    a2, d2, lv2 = map(int, input().split(' '))
    if lv2 % 2 == 0:
        golpeB = ((a2 + d2) / 2) + bonus
    else:
        golpeB = ((a2 + d2) / 2)
    if golpeA > golpeB:
        print('Dabriel')
    elif golpeA == golpeB:
        print('Empate')
    else:
        print('Guarte')
