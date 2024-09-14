lista = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Valor adicionado ao final da lista')
    if c == 1:
        if n > lista[0] or n == lista[0]:
            lista.append(n)
            print(f'Valor adicionado ao final da lista')
        else:
            lista.insert(0, n)
            print(f'O valor foi adicionado na posição 0')
    if c == 2:
        if n > lista[1] or n == lista[1]:
            lista.append(n)
            print(f'Valor adicionado ao final da lista')
        elif n < lista[1]:
            lista.insert(1, n)
            print(f'O valor foi adicionado na posição 1')
        elif n < lista[0]:
            lista.insert(0, n)
            print(f'O valor foi adicionado na posição 0')
    if c == 3:
        if n > lista[2] or n == lista[2]:
            lista.append(n)
            print(f'Valor adicionado ao final da lista')
        elif n < lista[0]:
            lista.insert(0, n)
            print(f'O valor foi adicionado na posição 0')
        elif n < lista[1]:
            lista.insert(1, n)
            print(f'O valor foi adicionado na posição 1')
        elif n < lista[2]:
            lista.insert(2, n)
            print(f'O valor foi adicionado na posição 2')
    if c == 4:
        if n > lista[3] or n == lista[3]:
            lista.append(n)
            print(f'Valor adicionado ao final da lista')
        elif n < lista[0]:
            lista.insert(0, n)
            print(f'O valor foi adicionado na posição 0')
        elif n < lista[1]:
            lista.insert(1, n)
            print(f'O valor foi adicionado na posição 1')
        elif n < lista[2]:
            lista.insert(2, n)
            print(f'O valor foi adicionado na posição 2')
        elif n < lista[3]:
            lista.insert(3, n)
            print(f'O valor foi adicionado na posição 3')
print('-='*20)
print(f'Os valores digitados em ordem foram {lista}')