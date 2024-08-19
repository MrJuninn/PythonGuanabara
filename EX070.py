totcom = totmais = baratopreço = 0
baratonome = ' '
while True:
    nome = str(input('Qual o nome do produto: ')).strip().title()
    preço = int(input('Qual o preço do produto: '))
    resp = ' '
    totcom += preço
    if preço > 1000:
        totmais += 1
    if baratonome == ' ' or preço < baratopreço:
        baratopreço = preço
        baratonome = nome
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O preço total da compra é R${totcom:.2f}')
print(f'O total de itens que custam mais de R$1000.00 é de {totmais}')
print(f'O produto mais barato foi {baratonome} que custa R${baratopreço:.2f}')
