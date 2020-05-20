n = int(input())
for i in range(0, n):
    ano = int(input())
    if ano > 2015:
        final = ano - 2014
        print('{} A.C.'.format(final))
    elif ano < 2015:
        final = 2015 - ano
        print('{} D.C.'.format(final))
    else:
        print('1 A.C.')
