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


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção:\033[m ')
    return opc