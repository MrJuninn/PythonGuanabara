from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        num = randint(1, 10)
        print(num, end=' ')
        lista.append(num)
        sleep(0.3)
    print('Pronto!')


def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {números}, temos {soma}')


números = []
sorteia(números)
soma_par(números)
