N = int(input())
cem = N // 100
resto_cem = N % 100
cinq = resto_cem // 50
rest_cinq = resto_cem % 50
vint = rest_cinq // 20
rest_vint = rest_cinq % 20
dez = rest_vint // 10
rest_dez = rest_vint % 10
cinco = rest_dez // 5
rest_cinco = rest_dez % 5
dois = rest_cinco // 2
rest_dois = rest_cinco % 2
um = rest_dois // 1
print(N)
print('{} nota(s) de R$ 100,00'.format(cem))
print('{} nota(s) de R$ 50,00'.format(cinq))
print('{} nota(s) de R$ 20,00'.format(vint))
print('{} nota(s) de R$ 10,00'.format(dez))
print('{} nota(s) de R$ 5,00'.format(cinco))
print('{} nota(s) de R$ 2,00'.format(dois))
print('{} nota(s) de R$ 1,00'.format(um))
