maiorp = 0
menorp = 0
for pessoa in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(pessoa)))
    if pessoa == 1:
        maiorp = peso
        menorp = peso
    else:
        if maiorp < peso:
            maiorp = peso
        elif peso < menorp:
            menorp = peso
print('O maior peso lido foi de {}Kg'.format(maiorp))
print('O menor peso lido foi de {}Kg'.format(menorp))
