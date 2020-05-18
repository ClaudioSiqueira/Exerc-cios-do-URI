N = int(input())
sinal = ''
par_impar = ''
for i in range(0, N):
    a = int(input())
    if a > 0 :
        sinal = 'POSITIVE'
    else:
        sinal = 'NEGATIVE'
    if a % 2 == 0:
        par_impar = 'EVEN '
    else:
        par_impar = 'ODD '
    if a == 0:
        sinal = 'NULL'
        par_impar =''
    print('{}{}'.format(par_impar, sinal))

