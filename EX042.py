print('\033[35mAnalisador de Triângulo v2\033[m')
print('=-'*13)
a = float(input('\033[33mPrimeiro Segmento:\033[m'))
b = float(input('\033[33mSegundo Segmento:\033[m'))
c = float(input('\033[33mTerceiro Segmento:\033[m'))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo')
    if a == b and b == c:
        print('\033[35mÉ um Triângulo Equilátero\033[m')
    elif a == b and b != c or a == c and c != b or b == c and a != c:
        print('\033[35mÉ um Triângulo Isósceles\033[m')
    elif a != b and b != c and c != a:
        print('\033[35mÉ um Triângulo Escaleno\033[m')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo')
