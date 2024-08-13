n = int(input('Digite um número:'))
print('=================')
d = n * 2
t = n * 3
r = n ** (1/2)
# Mantenha em mente a raiz quadrada 
print('>Dobro:\033[34m{}\033[m \n>Triplo:\033[31m{}\033[m \n>RaizQ:\033[35m{:.2f}\033[m'.format(d, t, r))
# A raiz quadrada pode ser exibida dessa forma aqui -> pow(n, (1/2))
