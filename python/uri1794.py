roupas = int(input())
la, lb = map(int, input().split(' '))
sa, sb = map(int, input().split(' '))
if la <= roupas <= lb and sa <= roupas <= sb:
    print('possivel')
else:
    print('impossivel')
