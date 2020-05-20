while True:
    c = int(input())
    if c == 0:
        break
    else:
        total = 0

        quantidade = ''
        quantidade2 = 0
        fruta = ''
        for i in range(c):
            frase = str(input())
            for num in frase:
                if num.isnumeric():
                    quantidade += num
            quantidade2 = int(quantidade)
            if 'suco de laranja' in frase:
                fruta = 120
            elif 'morango fresco' in frase:
                fruta = 85
            elif 'mamao' in frase:
                fruta = 85
            elif 'goiaba vermelha' in frase:
                fruta = 70
            elif 'manga' in frase:
                fruta = 56
            elif 'laranja' in frase:
                fruta = 50
            elif 'brocolis' in frase:
                fruta = 34
            total += quantidade2 * fruta
            quantidade = ''
        if total >= 130:
            resposta = total - 130
            print('Menos %i mg' % resposta)
        elif total <= 110:
            resposta = 110 - total
            print('Mais %i mg' % resposta)
        else:
            print(total, 'mg')
