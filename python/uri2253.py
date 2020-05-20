while True:
    try:
        lista = []
        maiusculo = 0
        minuscula = 0
        numero = 0
        n_pode = 0
        senha = str(input())
        for caracter in senha:
            lista.append(ord(caracter))
        if 6 <= len(lista) <= 32:

            for i in lista:
                if 65 <= i <= 90:
                    maiusculo += 1
                if 97 <= i <= 122:
                    minuscula += 1
                if 48 <= i <= 57:
                    numero += 1
                if i == 32 or i <= 47 or i >= 123 or 58 <= i <= 64 or 91 <= i <= 96:
                    n_pode += 1

            if minuscula >= 1 and maiusculo >= 1 and numero >= 1 and n_pode == 0:
                print('Senha valida.')
            else:
                print('Senha invalida.')

        else:
            print('Senha invalida.')

    except EOFError:
        break

