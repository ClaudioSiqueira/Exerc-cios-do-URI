while True:
    try:
        cont = 0
        n = int(input())
        if n == 1:
            print(0)
        else:
            while True:
                n = n/2
                cont += 1
                if n == 1:
                    break
            print(cont)
    except EOFError:
        break
