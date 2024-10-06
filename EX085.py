valores = [[], []]
for c in range(0,7):
    n = int(input(f'Digite o {c+1}° valor: '))
    if n % 2 == 0:
        valores[1].append(n)
    else:
        valores[0].append(n)
print(f'Os valores ímpares são {sorted(valores[0])}')
print(f'Os valores pares são {sorted(valores[1])}')
