cont = soma = contnum = 0
while cont != 999:
    cont = int(input('Digite um número [999 para parar]: '))
    if cont != 999:
        soma += cont
        contnum += 1
    else:
        print('Você digitou {} números e a soma entre eles foi {}.'.format(contnum, soma))
