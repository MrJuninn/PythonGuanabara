n1 = float(input('Primeira Nota:'))
n2 = float(input('Segunda Nota:'))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média foi {:.1f} \n\033[31mReprovado!\033[m'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi {:.1f} \n\033[34mRecuperação!\033[m'.format(media))
else:
    print('Sua média foi {:.1f} \n\033[35mAprovado!\033[m'.format(media))
