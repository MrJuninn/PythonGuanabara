frase = str(input('Escreva uma frase:')).strip()
ca = frase.upper().count('A')
pa = frase.upper().find('A') + 1
ua = frase.upper().rfind('A') + 1

print('A letra A aparece \033[35m{}\033[m vezes na frase'.format(ca))
print('A primeira letra A apareceu na posição \033[35m{}\033[m'.format(pa))
print('A última letra A apareceu na posição \033[35m{}\033[m'.format(ua))
