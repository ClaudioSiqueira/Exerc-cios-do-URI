cont_in = 0
cont_out = 0
N = int(input())
for i in range(0, N):
    a = int(input())
    if 10 <= a <= 20:
        cont_in += 1
    else:
        cont_out += 1
print('{} in'.format(cont_in))
print('{} out'.format(cont_out))

