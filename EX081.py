valores = []
total_num = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    total_num += 1
    resp = str(input('Deseja continuar ?[S/N] ')).strip().upper()[0]
    if 'N' in resp:
        break
print(f'Ao total foram {total_num} valores digitados')
print(f'A lista de valores em ordem decrescente é {sorted(valores, reverse=True)}')
if valores.count(5) > 0:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
    