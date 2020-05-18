tot_coelho = 0
tot_rato = 0
tot_sapo = 0
N = int(input())
for i in range(0, N):
    quantidade, animal = input().split(' ')
    quantidade = int(quantidade)
    animal = str(animal)

    if animal == 'C':
        tot_coelho += quantidade
    elif animal == 'R':
        tot_rato += quantidade
    elif animal == 'S':
        tot_sapo += quantidade
total = tot_sapo + tot_rato + tot_coelho

coelho_cem = (tot_coelho * 100)/total
rato_cem = (tot_rato * 100)/total
sapo_cem = (tot_sapo * 100)/total
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(tot_coelho))
print('Total de ratos: {}'.format(tot_rato))
print('Total de sapos: {}'.format(tot_sapo))
print('Percentual de coelhos: {:.2f} %'.format(coelho_cem))
print('Percentual de ratos: {:.2f} %'.format(rato_cem))
print('Percentual de sapos: {:.2f} %'.format(sapo_cem))




