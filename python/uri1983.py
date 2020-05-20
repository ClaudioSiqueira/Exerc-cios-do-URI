quant = int(input())
maior = 0
aluno_bom = ''
for i in range(0, quant):
    aluno, nota = map(float, input().split())
    if nota > maior:
        maior = nota
        aluno_bom = aluno
if maior >= 8:
    print('{:.0f}'.format(aluno_bom))
else:
    print('Minimum note not reached')
