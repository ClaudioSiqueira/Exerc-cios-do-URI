num = input().split('.')
zero = num[0]
um = num[1]
while True:
    if um[0] == '0':
        um = um[1:]
    else:
        break
print(um, end='')
print('.', end='')
print(zero)

