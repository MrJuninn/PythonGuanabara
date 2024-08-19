while True:
    cont = 0
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if n > 0:
        # Tabuada é criada aqui ↓
        while cont != 10:
            cont += 1
            print(f'{n} X {cont:2} = {n*cont}')
    else:
        break
    print('-'*20)
print('PROGRAMA TABUADA ENCERRADA')
