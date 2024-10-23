ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['média'] = float(input(f'Média de {ficha["nome"]}: '))
if ficha['média'] >= 7:
    ficha['situação'] = 'Aprovado'
elif 5 <= ficha['média'] < 7:
    ficha['situação'] = 'Recuperação'
else:
    ficha['situação'] = 'Reprovado'
print('-='*10)
for k, v in ficha.items():
    print(f'- {k} é igual a {v}')
