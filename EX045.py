from random import choice
from time import sleep
print('\033[35mJokenpô\033[m')
joken = ('Pedra', 'Papel', 'Tesoura')
print('\033[35m[0] Pedra\033[m')
print('\033[34m[1] Papel\033[m')
print('\033[36m[2] Tesoura\033[m')
escolha = choice(joken)
play = int(input('\033[33mO computador escolheu sua jogada, Sua vez!\033[m \n'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if escolha == joken[0]:  # Computador escolheu Pedra
    if play == 0:
        print('O computador escolheu {} e o jogador escolheu {} \n\033[33mEMPATE\033[m'.format(joken[0], joken[play]))
    elif play == 1:
        print('O computador escolheu {} e o jogador escolheu {} \n\033[32mVITÓRIA\033[m'.format(joken[0], joken[play]))
    elif play == 2:
        print('O computador escolheu {} e o jogador escolheu {} \n\033[31mDERROTA\033[m'.format(joken[0], joken[play]))
    else:
        print('\033[31mComando Invalido\033[m')
elif escolha == joken[1]:  # Computador escolheu Papel
    if play == 0:
        print('O computador escolheu {} e o jogador escolheu {} \n\033[31mDERROTA\033[m'.format(joken[1], joken[play]))
    elif play == 1:
        print('O computador escolheu {} e o jogador escolheu {} \n\033[33mEMPATE\033[m'.format(joken[1], joken[play]))
    elif play == 2:
        print('O computador escolheu {} e o jogador escolheu {} \n\033[32mVITÓRIA\033[m'.format(joken[1], joken[play]))
    else:
        print('\033[31mComando Invalido\033[m')
elif escolha == joken[2]:  # Computador escolheu Tesoura
    if play == 0:
        print('O computador escolheu {} e o jogador escolheu {} \n\033[32mVITÓRIA\033[m'.format(joken[2], joken[play]))
    elif play == 1:
        print('O computador escolheu {} e o jogador escolheu {} \n\033[31mDERROTA\033[m'.format(joken[2], joken[play]))
    elif play == 2:
        print('O computador escolheu {} e o jogador escolheu {} \n\033[33mEMPATE\033[m'.format(joken[2], joken[play]))
    else:
        print('\033[31mComando Invalido\033[m')
else:
    print('Comando Invalido')
