while True:
    try:
        cont = 0
        maior = ''
        menor = ''
        frase1 = str(input())
        frase2 = str(input())
        if len(frase1) > len(frase2):
            maior = frase1
            menor = frase2
        else:
            maior = frase2
            menor = frase1

        for letra in maior:
            if letra in menor:
                cont += 1
        print(cont)
    except EOFError:
        break
