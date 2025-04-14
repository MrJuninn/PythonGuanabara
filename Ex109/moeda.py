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
