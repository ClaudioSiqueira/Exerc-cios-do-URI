cont_par = 0
cont_impar = 0
cont_pos = 0
cont_neg = 0
for i in range(0, 5):
    a = float(input())
    if a % 2 == 0:
        cont_par += 1
    elif a % 2 == 1:
        cont_impar += 1
    if a > 0:
        cont_pos += 1
    elif a < 0:
        cont_neg += 1
print('{} valor(es) par(es)'.format(cont_par))
print('{} valor(es) impar(es)'.format(cont_impar))
print('{} valor(es) positivo(s)'.format(cont_pos))
print('{} valor(es) negativo(s)'.format(cont_neg))
