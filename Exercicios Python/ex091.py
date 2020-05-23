from random import randint
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)
}
ranking = []
print('Valores sorteados: ')
for k, v in jogo.items():
    print('{} tirou o valor {} no dado'.format(k, v))
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print('{}o lugar: {} com {}'.format(i + 1, v[0], v[1]))
