quant = int(input())
for i in range(quant):
    n, m = map(int, input().split(' '))
    total = n ** m
    total = str(total)
    print(len(total))