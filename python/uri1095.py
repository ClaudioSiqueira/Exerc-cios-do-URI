cont_i = 1
cont_j = 60
while True:
    print('I={} J={}'.format(cont_i, cont_j))
    cont_i += 3
    cont_j += -5
    if cont_j < 0:
        break
