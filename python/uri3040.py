quant = int(input())
for i in range(quant):
    altura, diametro, galhos = map(int, input().split(' '))
    if 200 <= altura <= 300 and diametro >= 50 and galhos >= 150:
        print('Sim')
    else:
        print('Nao')
