idade = int(input())
ano = idade // 365
ano_resto = idade % 365
mes = ano_resto // 30
mes_resto = ano_resto % 30
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(mes_resto))
