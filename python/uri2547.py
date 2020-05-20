while True:
    try:
        c, mini, maxi = map(int, input().split(' '))
        cont = 0
        for i in range(c):
            altura = int(input())
            if mini <= altura <= maxi:
                cont += 1
        print(cont)
    except EOFError:
        break
