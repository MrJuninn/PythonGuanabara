#frase = str(input('Digite uma frase: '))
#fraseo = frase.replace(' ', '').upper()
#print('O inverso de {} é {}'.format(fraseo, fraseo[::-1]))
#if fraseo == fraseo[::-1]:
#    print('Temos um palíndromo')
#else:
#   print('A frase digitada não é um palíndromo')
# Minha resolução sem o "For" ↑↑↑↑↑

frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
print(frase, inverso)
if inverso == frase:
    print(('Temos um palíndromo!'))
else:
    print('A frase digitada não é um palíndromo')
