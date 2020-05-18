i = 0
j = 1
cont = 0
while True:
  if i == 1.0:
    i = 1
  print('I={} J={}'.format(round(i, 2), round(j, 2)))
  cont += 1
  if cont == 3:
    i += 0.2
    j -= 3
    j += 0.2
    cont = 0
  j += 1
  if i >= 1:
    break

print('I=1 J=2')
print('I=1 J=3')
print('I=1 J=4')
i = 1.2
j = 2.2
while True:
  print('I={} J={}'.format(round(i, 2), round(j, 2)))
  cont += 1
  if cont == 3:
    i += 0.2
    j -= 3
    j += 0.2
    cont = 0
  j += 1
  if i >= 1.8:
    break

print('I=2 J=3')
print('I=2 J=4')
print('I=2 J=5')