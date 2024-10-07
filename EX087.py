matriz = [[], [], []]
soma = soma_coluna = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        n = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(n)
        if n % 2 == 0:
            soma += n
        if coluna == 2:
            soma_coluna += n
        if linha == 1 and n > maior or maior == 0:
            maior = n
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')
    print()
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {maior}')
