coluna, total = map(int, input().split())

i = 0
while True:
    i += 1
    for c in range(0, coluna):
        if c < coluna - 1:
            print(i, end=' ')
        else:
            print(i, end='')
        if i >= total:
            break
        i += 1
        if c == coluna - 1:
            i -= 1
    print('')
    if i >= total:
        break
