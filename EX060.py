fatorial = int(input('Digite um número para \ncalcular seu Fatorial: '))
fatorialc = 1
print('Calculando {}! = '.format(fatorial), end='')
while fatorial != 0:
    # Sobre o calculo, o que vai ser mostrado e o que vai ser calculado ↓
    if fatorial != 1:
        print('{} X '.format(fatorial),end='')               # print('{}'.format(c), end'')
        fatorialc *= fatorial                    # print(' x ' if c > 1 else ' = ', end='')
        fatorial -= 1
    # Sobre o sinal de igual no final ↓
    if fatorial == 1:
        print('{} = {}'.format(fatorial, fatorialc))
        fatorial -= 1
#
