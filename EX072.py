print('-='*10)
print('Números Por Extenso')
print('=-'*10)
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
player = int(input('Digite um valor entre 0 e 20 : '))
if player > 20 or player < 0:
    while player > 20 or player < 0:
        player = int(input('Tente Novamente, Digite um valor entre 0 e 20 : '))
print('=-'*10)
print(extenso[player])
