num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(num)
menor = min(num)
print('Você digitou os valores ', end='')
for i in num:
    print(f'{i}...', end='')
print()
print(f'O maior valor foi {maior} nas posições ', end='')
for p, n in enumerate(num):
    if n == maior:
        print(f'{p}...', end='')
print()
print(f'O menor valor foi {menor} nas posições ', end='')
for p, n in enumerate(num):
    if n == menor:
        print(f'{p}...', end='')
