import math


def eh_primo(n):
    # raiz = n**(0.5)
    raiz = int(math.sqrt(n))
    for d in range(2, raiz +1):
        if n % d == 0:
            return False
    return True

N = int(input())
for i in range(0, N):
    numero = int(input())
    if eh_primo(numero):
        print("{} eh primo".format(numero))
    else:
        print("{} nao eh primo".format(numero))
        