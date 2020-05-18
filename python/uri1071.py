maior = 0
impar = 0

x1 = int(input())
x2 = int(input())

if x1 > x2:
  maior = x1
  menor = x2
else:
  maior = x2
  menor = x1

for numeros in range(menor + 1, maior):
  if numeros % 2 == 1:
    impar = impar + numeros
print(impar)
