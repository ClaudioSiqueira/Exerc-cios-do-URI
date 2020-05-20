n = int(input())

t = 0.0

for i in range(n):
    p = input()
    p = p.split(' ')

    if int(p[0]) == 1001:
        t += int(p[1]) * 1.50
    elif int(p[0]) == 1002:
        t += int(p[1]) * 2.50
    elif int(p[0]) == 1003:
        t += int(p[1]) * 3.50
    elif int(p[0]) == 1004:
        t += int(p[1]) * 4.50
    elif int(p[0]) == 1005:   
        t += int(p[1]) * 5.50

print('%.2f' %t)