from time import sleep
sala = float(input('Qual é o salário do funcionário? R$'))
if sala > 1250:
    salafinal = sala + (sala * 10 / 100)
else:
    salafinal = sala + (sala * 15 / 100)
print('Analisando...')
sleep(2)
print('Quem ganhava R$\033[31m{:.2f}\033[m passa a ganhar R$\033[32m{:.2f}\033[m agora.'.format(sala, salafinal))
