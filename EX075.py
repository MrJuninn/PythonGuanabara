núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'O número 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O primeiro número 3 está na {núm.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados são: ', end='')
for _ in núm:
    if _ % 2 == 0:
        print(_, end=' ')
