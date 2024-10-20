dados = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    resp = str(input('Mais aluno para cadastrar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{'No.':<4}{'Nome':<10}{'Média':>8}')
print('-='*10)
for i, n in enumerate(dados):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8.1f}')
print('-='*10)
while True:
    num = int(input('Mostrar as notas de qual aluno? [999 Interrompe] '))
    if num == 999:
        break
    else:
        print(f'Notas de {dados[num][0]} são {dados[num][1]}')
