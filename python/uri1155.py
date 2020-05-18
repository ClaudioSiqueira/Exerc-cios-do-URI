soma = 1
for i in range(1, 101):
    conta = 1/i
    soma += conta
    i += 1
print('{:.2f}'.format(soma - 1))
