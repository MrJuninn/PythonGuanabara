print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 10
ct = 0
    #Lógica rústica de PA
while (contador > 0):
    print('{}'.format(primeiro), end='')
    print(' → ' if contador > 1 else ' → PAUSA ', end='')
    contador -= 1
    primeiro += razao
    ct += 1
    # Se chegar a 0 ele pergunta se vai querer mais termos.
    if contador == 0:
        print()
        contador = int(input('Quantos termos você quer mostrar a mais? '))
    # Se você pedir mais 0 termos ele finaliza com a contagem
    if contador == 0:
        print('Progressão realizada com {} termos mostrados'.format(ct))
