def aumentar(n=0, taxa=0, stats=False):
    res = n + (n * taxa / 100)
    if stats:
        return moeda(res)
    else:
        return res


def diminuir(n=0, taxa=0, stats=False):
    res = n - (n * taxa / 100)
    if stats:
        return moeda(res)
    else:
        return res


def dobro(n=0, stats=False):
    res = 2 * n
    if stats:
        return moeda(res)
    else:
        return res


def metade(n=0, stats=False):
    res = n / 2
    if stats:
        return moeda(res)
    else:
        return res


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, aum=10, dim=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum}% de aumento: \t{aumentar(n, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(n, dim, True)}')
    print('-' * 30)
