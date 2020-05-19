quant = int(input())
for i in range(quant):
    comida = float(input())
    dias = 0
    while True:
        dias += 1
        comida = comida / 2
        if comida <= 1:
            break
    print('%i dias' % dias)
