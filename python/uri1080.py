maior = 0
posicao = 0
for i in range(0, 100):
    a = int(input())
    if a > maior:
        maior = a
        posicao = i+1
print(maior)
print(posicao)
