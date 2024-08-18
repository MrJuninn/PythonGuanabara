cont = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma de todos os {cont} números deu {soma}')
