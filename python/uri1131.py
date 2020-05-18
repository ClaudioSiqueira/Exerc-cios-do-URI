vit_inter = 0
vit_gremio = 0
empate = 0
quantidade_grenal = 0
while True:
    inter, gremio = map(int, input().split())
    quantidade_grenal += 1
    if inter > gremio:
        vit_inter += 1
    elif gremio > inter:
        vit_gremio += 1
    else:
        empate += 1
    resposta = int(input('Novo grenal (1-sim 2-nao)\n'))
    if resposta == 2:
        break

print('{} grenais'.format(quantidade_grenal))
print('Inter:{}'.format(vit_inter))
print('Gremio:{}'.format(vit_gremio))
print('Empates:{}'.format(empate))
if vit_gremio > vit_inter:
    print('Gremio venceu mais')
elif vit_inter > vit_gremio:
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')


