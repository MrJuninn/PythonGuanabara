# Valores para a PA
pa = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
# Lógica para a PA
for c in range(pa, 10*raz, raz):
    print(c, end=(' - '))
print('Acabou')
