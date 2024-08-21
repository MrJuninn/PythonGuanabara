resp = 'S'
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    if resp in 'S':
        player = int(input('Digite um valor entre 0 e 20 : '))
        while 0 < player > 20:
            player = int(input('Tente Novamente, Digite um valor entre 0 e 20 : '))
        print('=-' * 10)
        print(f'Você digitou o número {extenso[player]}')
        resp = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    else:
        break
