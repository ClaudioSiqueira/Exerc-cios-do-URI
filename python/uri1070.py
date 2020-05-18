cont = 0
x = int(input())
for i in range(0, 12):
    if (x + cont) % 2 == 1:
        print(cont + x)
    cont += 1
