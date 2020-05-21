quant = int(input())
a = 0
e = 0
h = 0
m = 0
x = 0
for i in range(0, quant):
    personagem = input()
    if personagem[-1] == 'A':
        a += 1
    elif personagem[-1] == 'E':
        e += 1
    elif personagem[-1] == 'H':
        h += 1
    elif personagem[-1] == 'M':
        m += 1
    elif personagem[-1] == 'X':
        x += 1

print('{} Hobbit(s)'.format(x))
print('{} Humano(s)'.format(h))
print('{} Elfo(s)'.format(e))
print('{} Anao(s)'.format(a))
print('{} Mago(s)'.format(m))
