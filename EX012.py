print('===============')
print('D E S C O N T O')
print('===============')
p = float(input('Digite o preço do produto:'))
d = p * 5 / 100
print('O produto que custava \033[31mR${:.2f}\033[m, na promoção com desconto de 5% vai custar \033[35mR${:.2f}\033[m'.format(p, (p - d)))
