print('+=======================+')
print('Conversão Real para Dolar')
print('+=======================+')
r = float(input('Qual o valor que você deseja converter?R$'))
d = r / 3.27
print('===================================================')
print('O valor R$ \033[33m{}\033[m convertido em dolar é USD \033[35m{:.2f}'.format(r, d))
# Atualizar com o valor do dolar atual e mais moedas como euro e yene
