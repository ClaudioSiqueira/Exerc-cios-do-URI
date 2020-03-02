codigo, quant = input().split(' ')
codigo = int(codigo)
quant = int(quant)
if codigo == 1:
  total = 4 * quant
  print('Total: R$ {:.2f}'.format(total))
elif codigo == 2:
  total = 4.5 * quant
  print('Total: R$ {:.2f}'.format(total))
elif codigo == 3:
  total = 5 * quant
  print('Total: R$ {:.2f}'.format(total))
elif codigo == 4:
  total = 2 * quant
  print('Total: R$ {:.2f}'.format(total))
elif codigo == 5:
  total = 1.5 * quant
  print('Total: R$ {:.2f}'.format(total))
