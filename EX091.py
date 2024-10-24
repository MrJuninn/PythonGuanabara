from random import randint
from time import sleep
from operator import itemgetter
registro = dict()
ranking = list()
for c in range(0, 4):
    registro[f'jogador{c+1}'] = randint(0, 6)
    print(f'O Jogador {c+1} tirou {registro[f"jogador{c+1}"]} no dado.')
    sleep(1)
print('-='*15)
ranking = sorted(registro.items(), key=itemgetter(1), reverse=True)
print('   == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
