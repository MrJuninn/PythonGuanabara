print('{:-^20}'.format('BANCOS TAMA'))
print('-'*20)
valor = int(input('Qual o valor que você deseja sacar? R$'))
ced50 = ced20 = ced10 = ced1 = resto = 0
while True:
    if valor > 50:
        ced50 = valor // 50
        resto = valor - ced50 * 50
    if resto < 20:
        if resto % 10 == 0:
            ced10 = resto // 10
            resto = 0
        else:
            ced10 = resto // 10
            resto = resto - ced10 * 10
    else:
        ced20 = resto // 20
        resto = resto - ced20 * 20
    if resto / 1:
        ced1 = resto // 1
    if ced50 >= 1:
        print(f'Total de {ced50} cédulas de R$50')
    if ced20 >= 1:
        print(f'Total de {ced20} cédulas de R$20')
    if ced10 >= 1:
        print(f'Total de {ced10} cédulas de R$10')
    if ced1 >= 1:
        print(f'Total de {ced1} cédulas de R$1')
    break
print('-'*20)
