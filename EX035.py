print('=-'*20)
print('Analisador de Triângulos')
print('=-'*20)
a = float(input('Primeiro Segmento:'))
b = float(input('Segundo Segmento:'))
c = float(input('Terceiro Segmento:'))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo.')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo.')
