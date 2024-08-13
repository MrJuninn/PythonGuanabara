n = int(input('Digite um número para ver sua tabuada: '))
tab = int(input('Digite o número final da tabuada: '))
for c in range(1, tab+1):
    print('{} X {:2} = {}'.format(n, c, n * c))
