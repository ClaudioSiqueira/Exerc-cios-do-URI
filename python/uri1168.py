lista = [6, 2, 5, 5, 4 , 5, 6,  3, 7, 6]
quantidade = int(input())
for c in range(0, quantidade):
  n = str(input())
  total = 0
  for i in n:
    i = int(i)
    total += lista[i]

  print('{} leds'.format(total))
