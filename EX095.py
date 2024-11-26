jogadores = list()
jogador = dict()
jogos = list()
resp = 'S'
while resp == 'S':
    jogador.clear()
    jogos.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(quant):
        jogos.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = jogos[:]
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('-='*20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for c, v in enumerate(jogadores):
    print(f'{c:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*20)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe um jogador com o código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*20)
print('VOLTE SEMPRE')
