while True:
    c = int(input())
    if c == 0:
        break
    pontos_a = pontos_b = 0
    for i in range(c):
        a, b = map(int, input().split(' '))
        if a > b:
            pontos_a += 1
        elif a < b:
            pontos_b += 1
    print('{} {}'.format(pontos_a, pontos_b))
