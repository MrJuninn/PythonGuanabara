matriz = [[], [], []]
for c in range(0, 3):
    for i in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {i}]: '))
        matriz[c].append(n)
print('-='*30)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[ {matriz[c][i]:^5} ]', end='')
    print()
