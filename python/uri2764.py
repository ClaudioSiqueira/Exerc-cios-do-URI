while True:
    try:
        dia, mes, ano = map(str, input().split('/'))
        print('{}/{}/{}'.format(mes, dia, ano))
        print('{}/{}/{}'.format(ano, mes, dia))
        print('{}-{}-{}'.format(dia, mes, ano))
    except EOFError:
        break
