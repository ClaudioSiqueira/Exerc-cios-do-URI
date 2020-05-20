a, b = map(int, input().split())
total = a
for i in range(0, b):
    msg = str(input())
    if msg == 'fechou':
        total += 1
    else:
        total -= 1
print(total)
