while True:
    try:
        string = str(input())
        if string == 'esquerda':
            print('ingles')
        elif string == 'direita':
            print('frances')
        elif string == 'nenhuma':
            print('portugues')
        else:
            print('caiu')
    except EOFError:
        break