fatorial = int(input('Digite um número: '))
fatorialc = 1
while fatorial != 0:
    print('{}x'.format(fatorial),end='')
    fatorialc = fatorialc * fatorial
    fatorial = fatorial - 1

