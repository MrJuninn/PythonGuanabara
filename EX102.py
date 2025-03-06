def fatorial(n, show=False):
    '''
    → Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                return f' = {f}'
        else:
            if c == 1:
                return f

print(fatorial(4, True))
help(fatorial)
