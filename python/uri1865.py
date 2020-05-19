quant = int(input())
for i in range(quant):
    msg = str(input())
    if msg[:4] == 'Thor':
        print('Y')
    else:
        print('N')