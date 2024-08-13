print('\033[1;32m=§\033[m'*10)
print('\033[1;33mAlistamento Militar\033[m')
print('\033[1;32m=§\033[m'*10)
nasc = int(input('Em qual ano você nasceu?:'))
if 2024 - nasc == 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, 2024 - nasc, 2024))
    print('\033[32mEstá na hora de se alistar\033[m')
elif 2024 - nasc < 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, 2024 - nasc, 2024))
    print('Ainda não está na hora de se alistar')
    print('\033[36mFaltam {} anos ainda\033[m'.format(18-(2024-nasc)))
    print('Seu alistamento será em {}'.format(nasc + 18))
else:
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, 2024 - nasc, 2024))
    print('Já passou da hora de se alistar')
    print('\033[31mJá passou {} anos da hora de se alistar\033[m'.format(2024-nasc-18))
    print('Seu alistamento foi em {}'.format(nasc + 18))
