while True:
    n = int(input())
    total = 0
    if n == 0:
        break
    for i in range(1, n + 1):
        total += (i ** 2)
    print(total)
