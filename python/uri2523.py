while True:
    try:
        frase = ''
        alfabeto = input()
        c = int(input())
        lista = list(map(int, input().split(' ')))
        for i in range(c):
            letra = alfabeto[lista[i] - 1]
            frase += letra
        print(frase)
    except EOFError:
        break
