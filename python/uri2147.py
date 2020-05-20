quant = int(input())
for i in range(quant):
    total = 0
    frase = input()
    for letra in frase:
        total += 0.01
    print('{:.2f}'.format(total))
