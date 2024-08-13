from math import sqrt
print('='*21)
print('CALCULO DA HIPOTENUSA')
print('='*21)
co = float(input('\033[31mQual o comprimento do cateto oposto:\033[m'))
ca = float(input('\033[34mQual o comprimento do cateto adjacente:\033[m'))
print('\033[35mO valor da hipotenusa é \033[4;35m{:.2f}'.format(sqrt(co**2 + ca**2)))
# Guanabara criou uma variante para a hipotenusa que é a "hi = (co ** 2 + ca ** 2) ** (1/2) que é a raiz quadrada das somas dos catetos(Porem eu acertei da forma que fiz sem a ajuda rs)
# e eu não li a biblioteca e isso me custou saber sobre isso math.hypot(co, ca) isso é o modulo da hipotenusa e com isso sei fazer de 3 formas agora
