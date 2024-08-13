dist = int(input('Qual a distancia da sua viagem?'))
if dist > 200:
    multa = dist * 0.45
    print('O valor da viagem é R$\033[35m{:.2f}\033[m'.format(multa))
else:
    multa = dist * 0.50
    print('O valor da viagem é R$\033[35m{:.2f}\033[m'.format(multa))
