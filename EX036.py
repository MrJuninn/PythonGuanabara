print('Empréstimo Bancário')
casa = float(input('Qual o valor da casa que você deseja comprar?:'))
salario = float(input('Qual o valor do seu salário?:'))
anos = int(input('Em quantos anos você irá pagar?:'))
meses = anos * 12
parcela = casa / meses
if parcela <= (salario * 30 / 100):
    print('O empréstimo foi \033[32mCONCLUÍDO\033[m e o valor da parcela é R$\033[35m{:.2f}\033[m'.format(parcela))
elif parcela > (salario * 30 / 100):
    print('O empréstimo foi \033[31mNEGADO\033[m')
