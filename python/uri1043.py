A, B, C = input().split(' ')

A = float(A)
B = float(B)
C = float(C)

if A + B > C and A + C > B and B + C > A:
    perimetro = A + B + C
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    area = ((A + B)* C)/2
    print('Area = {:.1f}'.format(area))


