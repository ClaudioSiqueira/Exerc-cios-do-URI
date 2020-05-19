while True:
    try:
        a, b, c = map(int, input().split(' '))
        if a == b == c:
            print('*')
        else:
            if a != b and a != c:
                print('A')
            elif b != a and b != c:
                print('B')
            elif c != a and c != b:
                print('C')
    except EOFError:
        break
