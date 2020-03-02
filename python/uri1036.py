from math import sqrt
A, B, C = input().split(' ')
A = float(A)
B = float(B)
C = float(C)
delta = (B**2) - (4 * A * C)
if delta < 0 or A == 0:
  print('Impossivel calcular')
else:
  r1 = (-B + sqrt(delta))/(2 * A)
  print('R1 = {:.5f}'.format(r1))
  r2 = (-B - sqrt(delta))/(2 * A)
  print('R2 = {:.5f}'.format(r2))
  