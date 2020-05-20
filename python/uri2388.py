quant = int(input())
total = 0
for i in range(0, quant):
    a, b = (map(int, input().split()))
    total += a * b
print(total)
