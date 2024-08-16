media = 0
homem = ''
homemidade = 0
mulher = 0
for c in range(1,5):
    print('----- {}ª PESSOA ------'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    # Homem mais velho e mulher mais nova
    if sexo == 'M' and idade > homemidade:
        homem = nome
        homemidade = idade
    if sexo == 'F' and idade < 20:
        mulher += 1
print('A média de idade do grupo é de {} anos'.format(media / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(homemidade, homem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
