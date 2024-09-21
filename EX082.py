valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if 'N' in resp:
        for pos, c in enumerate(valores):
            if valores[pos] % 2 == 0:
                pares.append(valores[pos])
            else:
                impares.append(valores[pos])
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
