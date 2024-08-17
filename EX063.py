print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
termos = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
c = 0
# Fibonacci do krl
while termos != 0:
    print('{} → '.format(c), end='')
    a = b
    b = a + c
    c = a
    termos -= 1
print('FIM')
