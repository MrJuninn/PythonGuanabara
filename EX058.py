from random import randint
n = randint(0, 10)
jogador = 11
contador = 0
print('Sou seu computador... \nAcabei de pensar em um número de 0 a 10. \nSerá que você consegue adivinhar qual foi?')
while jogador != n:
    jogador = int(input('Qual é o seu palpite? '))
    if jogador > n:
        print('Menos... Tente mais uma vez.')
    if jogador < n:
        print('Mais... Tente mais uma vez.')
    contador += 1
print('Acertou com {} tentativas. Parabéns'.format(contador))
