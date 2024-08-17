print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 0
while (contador < 10):
    print('{}'.format(primeiro), end='')
    print(' → ' if contador < 9 else ' → FIM ', end='')
    contador += 1
    primeiro += razao
