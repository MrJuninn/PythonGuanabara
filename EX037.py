num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opc = int(input('Sua opção:'))
if opc == 1:
    print('{} convertido para BINÁRIO é igual a \033[35m{}\033[m'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para OCTAL é igual a \033[35m{}\033[m'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} convertido para HEXADECIMAL é igual a \033[35m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('Comando Inválido, Tente Novamente')
