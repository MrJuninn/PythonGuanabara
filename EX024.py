nome = str(input('Digite o nome da cidade?')).strip()
print('O nome da cidade começa com Santos?:\033[35m{}\033[m'.format((nome[:5].upper() == 'SANTO')))
