def main():
    N = int(input())
    for i in range(N):
        frase = input().upper()
        contador = 0
        alfabeto = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for letra in alfabeto:
            if letra in frase:
                contador += 1
        if contador == 26:
            print('frase completa')
        elif contador >= 13:
            print('frase quase completa')
        else:
            print('frase mal elaborada')

main()
