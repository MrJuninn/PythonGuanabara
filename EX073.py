times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Bahia', 'São Paulo', 'Cruzeiro', 'Atlético-MG', 'Athletico-PR', 'Vasco', 'Juventude', 'Bragantino', 'Internacional', 'Criciúma', 'Grêmio', 'EC Vitória', 'Corinthians', 'Fluminense', 'Cuiabá', 'Atlético-GO')
print(f'Tabela do Brasileirão → {times}')
print('-='*50)
print(f'Os 5 primeiros colocados → {times[0:5]}')
print('-='*50)
print(f'Os 4 últimos colocados → {times[16:]}')    # [-4:]
print('-='*50)
print(f'Times em ordem alfabética → {sorted(times)}')
print('-='*50)
print(f'O Vasco está na {times.index('Vasco')+1}° posição')
