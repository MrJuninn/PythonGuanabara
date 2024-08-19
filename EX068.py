from random import randint
print('-'*15)
print('Impar ou Par')
print('-'*15)
cont = 0
while True:
    valor = int(input('Diga um valor: '))
    computador = randint(0, 10)
    pi = (computador + valor) % 2
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    if pi == 0:
        print(f'Você jogou {valor} e o computador {computador}. Total de {valor+computador} DEU PAR')
        print('-'*20)
    else:
        print(f'Você jogou {valor} e o computador {computador}. Total de {valor+computador} DEU IMPAR')
        print('-'*20)
    if pi == 0 and escolha == 'P' or pi == 1 and escolha == 'I':
        print('Você VENCEU')
        print('Vamos jogar novamente')
        print('-'*20)
        cont += 1
    else:
        print('Você PERDEU!')
        print('-='*20)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
