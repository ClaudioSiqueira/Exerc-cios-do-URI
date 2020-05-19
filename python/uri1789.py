while True:
    try:
        total = int(input())
        vetor = [0] * total
        msg = str(input())
        maior = 0
        vetor = msg.split(' ')
        vetor_int = []
        for i in vetor:
            vetor_int.append(int(i))
        for elemento in vetor_int:
            if elemento > maior:
                maior = elemento
            if maior < 10:
                resposta = 1
            elif 10 <= maior < 20:
                resposta = 2
            else:
                resposta = 3
        print(resposta)
    except EOFError:
        break