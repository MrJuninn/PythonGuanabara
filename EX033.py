num1 = int(input('Primeiro Valor:'))
num2 = int(input('Segundo Valor:'))
num3 = int(input('Terceiro Valor:'))
main = 0
menon = 0
if num1 < num2:
    menon = num1
    main = num2
else:
    main = num1
    menon = num2
if num3 < menon:
    menon = num3
if main < num3:
    main = num3
print('O menor valor digitado foi \033[34m{}\033[m'.format(menon))
print('O maior valor digitado foi \033[31m{}\033[m'.format(main))
