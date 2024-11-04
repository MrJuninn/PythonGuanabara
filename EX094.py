dados = dict()
ficha = list()
acima = list()
media = totida = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            dados['idade'] = int(input('Idade: '))
            totida += dados['idade']
            ficha.append(dados.copy())
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    while True:
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    media = totida / len(ficha)
    if resp in 'N':
        for c in ficha:
            for i, v in c.items():
                if i == 'idade' and v > media:
                    acima.append(c)
        break
print(f'A)  Ao todo temos {len(ficha)} pessoas cadastradas.')
print(f'B)  A média de idade é {media:5.2f} anos.')
print('C)  As mulheres cadastradas foram ', end='')
for p in ficha:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D)  Lista de pessoas que estão acima da média:')
for c in acima:
    for i, v in c.items():
        print(f' {i} = {v}', end=';')
    print()
