# Valores para a PA
pa = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
décimo = pa + (10 - 1) * raz
# Lógica para a PA
for c in range(pa, décimo + raz, raz):
    print(c, end=(' - '))
print('Acabou')
