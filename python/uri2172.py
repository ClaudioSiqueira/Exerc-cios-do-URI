while True:
    try:
        n1, n2 = map(int, input().split(' '))
        if n1 != 0 and n2 != 0:
            print(n1 * n2)
    except EOFError:
        break
