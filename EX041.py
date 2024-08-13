print('\033[35mConfederação Nacional de Natação\033[m')
print('\033[31m=-\033[m'*16)
nasc = int(input('Qual seu ano de nascimento?:'))
idade = 2024 - nasc
if idade <= 9:
    print('Sua categoria é \033[35mMirim\033[m')
elif idade <= 14:
    print('Sua categoria é \033[35mInfantil\033[m')
elif idade <= 19:
    print('Sua categoria é \033[35mJunior\033[m')
elif idade <= 25:
    print('Sua categoria é \033[35mSênior\033[m')
else:
    print('Sua categoria é \033[35mMaster\033[m')
