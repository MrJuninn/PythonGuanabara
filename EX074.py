from random import randint
num = tuple(randint(0, 10) for _ in range(5))
print(f'Os valores Sorteados são: ', end= '')
for n in num:
    print(f'{n} ', end='')
print()
print(f'O maior valor sorteado é {max(num)}')
print(f'O menor valor sorteado é {min(num)}')
