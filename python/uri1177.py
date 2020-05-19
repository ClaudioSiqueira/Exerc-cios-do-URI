vetor = []
n = int(input())
while True:
    if len(vetor) > 1000:
        break
    for j in range(0, n):
        vetor.append(j)
    if len(vetor) > 1000:
        break
for indice, valor in enumerate(vetor):
    if indice == 1000:
        break
    print('N[{}] = {}'.format(indice, valor))
