def leiaint(valor):
    ok = False
    v = 0
    while True:
        n = str(input(valor))
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            print('\033[0:31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return v


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
