from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p == 0:
        p = 1
    if f <= i:
        for c in range(i, f - p, -p):
            if c < f:
                break
            print(f'{c} ', end='')
            sleep(0.5)
    if f >= i:
        for c in range(i, f + p, p):
            print(f'{c} ', end='')
            sleep(0.5)
    print('FIM!')
    print('-=' * 20)

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, abs(passo))
