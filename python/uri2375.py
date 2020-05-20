n = int(input())
a, b, c = map(int, input().split(' '))
if a >= n and b >= n and c >= n:
    print('S')
else:
    print('N')
