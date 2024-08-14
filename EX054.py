from datetime import date
maiori = 0
menori = 0
ano = date.today().year
for c in range(1, 8):
    pessoa = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = ano - pessoa
    if idade >= 18:
        maiori += 1
    else:
        menori += 1
if maiori >= 1 and menori >= 1:
    print('Ao todo tivemos {} pessoas maiores de idade \nE também tivemos {} pessoas menores de idade'.format(maiori, menori))
elif maiori >= 1 and menori == 0:
    print('Ao todo tivemos {} pessoas maiores de idade'.format(maiori))
elif menori >= 1 and maiori >= 0:
    print('Ao todo tivemos {} pessoas menores de idade'.format(menori))
