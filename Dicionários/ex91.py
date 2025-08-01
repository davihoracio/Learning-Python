from random import randint
from time import  sleep
from operator import itemgetter, invert

jogo = {'Jogador1': randint(1,10),
        'Jogador2': randint(1,10),
        'Jogador3': randint(1, 10),
        'Jogador4': randint(1,10)}
rank = []
for k, v in jogo.items():
    print(f'O {k} está com {v}')
rank = sorted(jogo.items(), key= itemgetter(1), reverse=True)
print(rank)
for k, v in enumerate(rank):
    print(f'{k+1}°: {v[0]} com {v[1]}')