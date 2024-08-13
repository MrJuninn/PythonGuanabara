print('\033[1;30;46mComparar Valores\033[m')
n1 = int(input('Primeiro Valor:'))
n2 = int(input('Segundo Valor:'))
if n1 > n2:
    print('O primeiro valor é \033[;31mMaior\033[m')
elif n2 > n1:
    print('O segundo valor é \033[;31mMaior\033[m')
else:
    print('Não existe valor maior, Os dois são \033[;36miguais\033[m')
