from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
escolha = 0
while escolha != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    escolha = int(input('>>>>> Qual é a sua opção? '))
    if escolha == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    if escolha == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    if escolha == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
    if escolha == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    if escolha not in (1,2,3,4,5):
        print('Opção invalida, Tente novamente')
    print('=-=='*6)
print('Finalizando...')
sleep(2)
print('Fim do programa! Volte sempre!')
