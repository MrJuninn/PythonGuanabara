lista = []
while True:
    listaadd = int(input('Digite um valor: '))
    if listaadd in lista:
        print('Valor duplicado, não vou adicionar')
    else:
        print('Valor adicionado com sucesso')
        lista.append(listaadd)
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if 'N' in escolha:
        break
print(f'Você digitou os valores {sorted(lista)}')
