from math import sqrt

n = int(input())
final = ((((1 + sqrt(5)) / 2) ** n) - (((1 - sqrt(5)) / 2) ** n)) / sqrt(5)
print('%.1f' % final)