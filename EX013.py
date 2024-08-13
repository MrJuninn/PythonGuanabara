print('Salário')
print('=======')
S = float(input('Digite o seu salário R$'))
AS = S * 15 / 100
print('Seu novo salário é R$\033[32m{:.2f}'.format(S + AS))
