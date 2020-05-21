while True:
    try:
        lista = ['nada']
        for i in range(0, 10):
            nome = str(input())
            lista.append(nome)
        print(lista[3])
        print(lista[7])
        print(lista[9])
    except EOFError:
        break
