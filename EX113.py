def leiaint(valor):
    while True:
        try:
            n = int(input(valor))
            return n
        except KeyboardInterrupt:
            print('\n\033[;31mUsuário preferiu não digitar esse número\033[m')
            return 0
        except:
            print('\033[;31mERRO: Por favor, digite um número inteiro válido.\033[m')


def leiafloat(valor):
    while True:
        try:
            n = float(input(valor))
            return n
        except KeyboardInterrupt:
            print('\n\033[;31mUsuário preferiu não digitar esse número\033[m')
            return 0
        except:
            print('\033[;31mERRO: Por favor, digite um número real válido.\033[m')


n1 = leiaint('Digite  um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
