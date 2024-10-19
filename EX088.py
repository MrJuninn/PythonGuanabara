from random import sample
from time import sleep
palpites = []
print('='*30)
print('      JOGA NA MEGA SENA')
print('='*30)
quantidade = int(input('Quantos jogos você vai fazer?: '))
for contador in range(quantidade):
    números = sample(range(1, 60), 6)
    palpites.append(números[:])
    números.clear()
print('-='*3, f'SORTEANDO {quantidade} JOGOS', '-='*3)
for contador in range(quantidade):
    print(f'Jogo {contador+1}: {sorted(palpites[contador])}')
    sleep(1)
print('-='*5, '< BOA SORTE >', '-='*5)
