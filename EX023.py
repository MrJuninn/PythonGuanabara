num = int(input('Digite um número entre 0 e 9999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade:\033[35m{}\033[m \nDezena:\033[35m{}\033[m \nCentena:\033[35m{}\033[m \nMilhar:\033[35m{}\033[m'.format(u, d, c, m))

#Esqueci real da matematica nessa
