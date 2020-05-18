cont_i = 1
cont_j = 7
while True:
    print('I={} J={}'.format(cont_i, cont_j))
    cont_j += -1
    if cont_j < 5:
        cont_i = 3
        cont_j = 9
        break
while True:
    print('I={} J={}'.format(cont_i, cont_j))
    cont_j += -1
    if cont_j < 7:
        cont_i = 5
        cont_j = 11
        break
while True:
    print('I={} J={}'.format(cont_i, cont_j))
    cont_j += -1
    if cont_j < 9:
        cont_i = 7
        cont_j = 13
        break
while True:
    print('I={} J={}'.format(cont_i, cont_j))
    cont_j += -1
    if cont_j < 11:
        cont_i = 9
        cont_j = 15
        break
while True:
    print('I={} J={}'.format(cont_i, cont_j))
    cont_j += -1
    if cont_j <= 12:
        cont_i = 9
        cont_j = 17
        break
