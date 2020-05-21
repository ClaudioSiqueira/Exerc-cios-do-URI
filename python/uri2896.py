quant = int(input())
for i in range(quant):
    a, b = map(int, input().split(' '))
    print((a % b) + (a // b))


