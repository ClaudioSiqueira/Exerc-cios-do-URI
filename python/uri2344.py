num = int(input())
resposta = ''
if num == 0:
    resposta = 'E'
elif 1 < num <= 35:
    resposta = 'D'
elif 36 < num <= 60:
    resposta = 'C'
elif 61 < num <= 85:
    resposta = 'B'
else:
    resposta = 'A'
print(resposta)
