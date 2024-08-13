velo = float(input('Qual a velocidade do seu carro?(km):'))
if velo > 80:
    multa = velo - 80
    print('\033[31mVocê ultrapassou o limite e sua multa é de R${:.2f}\033[m'.format(multa * 7))
else:
    print('\033[32mSua situação está ok\033[m')

