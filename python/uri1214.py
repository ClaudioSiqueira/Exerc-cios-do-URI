c = int(input())
lista = []
numeros = ''
total = 0
cont = 0
soma = 0
alunos = 0
for i in range(c):
    numeros = input().split(' ')
    for j in numeros:
        lista.append(int(j))
        if cont != 0:
            soma += int(j)
        cont += 1
    total = lista[0]
    del(lista[0])
    media = (soma / total)
    for k in lista:
        if k > media:
            alunos += 1
    final = (alunos * 100) / total
    print('{:.3f}%'.format(final))
    lista.clear()
    cont = alunos = total = soma = 0
