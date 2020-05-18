n = int(input())
t1 = 0
t2 = 1
if n == 1:
  print('{}'.format(t1))
elif n == 2:
  print('{} {}'.format(t1, t2))
else:
  cont = 3
  print('{} {}'.format(0, 1), end= ' ')
  while cont < n:
    t3 = t1 + t2
    print('{}'.format(t3), end= ' ')
    t1 = t2
    t2 = t3
    cont += 1
  print(t3 + t1)