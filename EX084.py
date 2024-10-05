pessoas = list()
dados = list()
maior = menor  = 0
maiornome = list()
menornome = list()
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    pessoas.append(dados[:])
    dados.clear()
    if 'N' in resp:
        break
for i, p in enumerate(pessoas):
    if i == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]
for i, p in enumerate(pessoas):
    if p[1] == maior:
        maiornome.append(p[0])
    elif p[1] == menor:
        menornome.append(p[0])
print(f'Ao todo foi cadastrado {len(pessoas)} pessoas')
print(f'A pessoa com o maior peso é ', end='')
for p in maiornome:
    print(f'[{p}] ', end='')
print(f'com {maior}kgs')
print(f'A pessoa com o menor peso é ', end='')
for p in menornome:
    print(f'[{p}] ', end='')
print(f'com {menor}kgs')
