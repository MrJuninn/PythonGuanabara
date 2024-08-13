from random import randint
from time import sleep
print('Pensei em um número')
n = randint(0,5)
nu = int(input('Adivinhe o número que eu pensei:'))
print('Processando...')
sleep(3)
print('\033[33mEu pensei em {}\033[m'.format(n))
if nu == n:
    print('\033[35mVocê acertou o número parabéns!\033[m')
else:
    print('\033[31mVocê errou que pena\033[m')
