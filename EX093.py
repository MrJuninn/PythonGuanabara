jogador = dict()
jogos = list()
jogador['nome'] = str(input('Nome do jogador: '))
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(quant):
    jogos.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = jogos[:]
jogador['total'] = sum(jogador['gols'])
print('-='*20)
print(jogador)
print('-='*20)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {quant} partidas.')
for i, v in enumerate(jogos):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
