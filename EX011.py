print('==============')
print('Quantos Litros')
print('==============')
L = float(input('Digite a largura da parede:'))
A = float(input('Digite a altura da parede:'))
MQ = L * A
print('Sua parede tem a dimensão de \033[31m{}\033[mx\033[31m{}\033[m e sua área é de \033[35m{}m²\033[m'.format(L, A, L*A))
print('E será necessário \033[31m{}\033[mL de tinta'.format(MQ / 2))
