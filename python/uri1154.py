cont = 0
soma = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    cont += 1
    soma += idade
print('{:.2f}'.format(soma/cont))
