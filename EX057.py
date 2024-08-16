'''sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu sexo? [M/F]:')).upper()
    if sexo != 'M' and sexo != 'F':
        print('\033[31mValor Invalido, Tente Novamente\033[m')
    if sexo == 'M':
        print('Seu sexo é \033[33mMASCULINO\033[m')
    if sexo == 'F':
        print('Seu sexo é \033[35mFEMININO\033[m')
print('Acabou')'''
# Minha resolução ↑

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo =  str(input('Informe seu sexo: [M/F] ')).upper()
    if sexo != 'M' and sexo != 'F':
        while sexo != 'M' and sexo != 'F':
            sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
    if sexo == 'M':
            print('Sexo M registrado com sucesso')
    if sexo == 'F':
            print('Sexo F registrado com sucesso')

# Fiz sozin :b ambos