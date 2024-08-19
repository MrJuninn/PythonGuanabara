maisidade = homens = mulheres = 0
while True:
    idade = int(input('Qual a idade da pessoa? '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Qual o sexo da pessoa? ')).strip()[0]
    if idade > 18:
        maisidade += 1
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        mulheres += 1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Ss':
        print('-'*20)
    else:
        break
print(f'O número de pessoas acima de 18 anos foi de {maisidade}')
print(f'O número de homens cadastrados foi de {homens}')
print(f'O número de mulheres que tem menos de 20 anos foi de {mulheres}')
print('Fim do programa')
