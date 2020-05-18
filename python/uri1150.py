x = int(input())
cont = 1
while True:
    z = int(input())
    if z > x:
        break
x2 = x
while True:
    x += x2
    cont += 1
    if x > z:
        break
    else:
        x2 += 1
print(cont)
