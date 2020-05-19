quantidade = int(input())
for c in range(0, quantidade):
  msg = str(input())
  direita = int(input())
  lista_msg = []
  for letra in msg:
    num = ord(letra) - direita
    if num < 65:
      num = num + 26
    lista_msg.append(num)
  for i in lista_msg:
    print(chr(i), end ='')
  print('')