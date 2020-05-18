primeiro = input()
segundo = input()
terceiro = input()

if primeiro == 'vertebrado' and segundo == 'ave' and terceiro == 'carnivoro':
    print('aguia')
elif primeiro == 'vertebrado' and segundo == 'ave' and terceiro == 'onivoro':
    print('pomba')
elif primeiro == 'vertebrado' and segundo == 'mamifero' and terceiro == 'onivoro':
    print('homem')
elif primeiro == 'vertebrado' and segundo == 'mamifero' and terceiro == 'herbivoro':
    print('vaca')
elif primeiro == 'invertebrado' and segundo == 'inseto' and terceiro == 'hematofago':
    print('pulga')
elif primeiro == 'invertebrado' and segundo == 'inseto' and terceiro == 'herbivoro':
    print('lagarta')
elif primeiro == 'invertebrado' and segundo == 'anelideo' and terceiro == 'hematofago':
    print('sanguessuga')
else:
    print('minhoca')
