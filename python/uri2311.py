c = int(input())
for i in range(c):
    maior = 0
    menor = 11
    nome = input()
    vezes = float(input())
    notas_str = list(input().split(' '))
    notas_int = []
    for n in notas_str:
        notas_int.append(float(n))
    for num in notas_int:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma = sum(notas_int) - menor - maior
    resposta = soma * vezes
    print('{} {:.2f}'.format(nome, resposta))
