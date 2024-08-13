nome = str(input('Digite o seu nome completo:')).strip().split()
pn = nome[0]
un = nome[len(nome)-1]
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é \033[35m{}\033[m.'.format(pn))
print('Seu último nome é \033[31m{}\033[m.'.format(un))
