resp = ''
soma = cont = maior = menor = 0
while resp == '' or resp == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if resp == '':
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
print('Você digitou {} números e a média foi {:.2f}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
