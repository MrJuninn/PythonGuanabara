ano = int(input('Digite o ano que deseja verificar:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mEle é bissexto\033[m')
else:
    print('\033[31mEle não é  bissexto\033[m')
