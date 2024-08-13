num = float(input('Digite um número:'))
print('o numero \033[31m{}\033[m tem a parte inteira \033[35m{}'.format(num, round(num)))
# pode usar trunc(num) ou int(num) tambem
# o round(num) que eu usei ele não é bom nesse exemplo pois ele arredonda para o número inteiro mais proximo ex: 6.525 ele vira 7 pois esta acima de meio o valor decimal.
