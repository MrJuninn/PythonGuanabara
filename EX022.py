from time import sleep
nome = str(input('\033[31mDigite seu nome completo:\033[m'))
print('\033[33mAnalisando seu nome...\033[m')
sleep(3)
print('O nome em letras maiusculas: \033[35m{}\033[m'.format(nome.upper()))
sleep(1)
print('O nome em letras minusculas: \033[35m{}\033[m'.format(nome.lower()))
sleep(1)
num = nome.split()
print('O número de letras sem contar com espaço \033[35m{}\033[m'.format(len(nome.replace(' ', ''))))
sleep(1)
print('O primeiro nome tem \033[35m{}\033[m letras'.format(len(num[0])))

# O gustavo guanabara tirou o espaço do meio com isso aqui
# nome = str(input('Digite seu nome completo')).strip() -> isso tira os espaços da frente e de tras do nome
# .format(len(nome) - nome.count(' ')) -> esse é pra tirar o espaço que sobrou ex: se o nome tem 3 espaços no meio o len vai contar as letras e diminuir com o numero de espaços
