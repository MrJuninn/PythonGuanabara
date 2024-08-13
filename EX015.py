print('\033[35mAluguel de carros\033[m')
print('\033[31m-\033[m'*17)
d = int(input('\033[33mQuantos dias alugados? '))
km = float(input('\033[33mQuantos km rodados? '))
dp = d * 60
kp = km * 0.15
print('\033[33mO total a pagar é de R$\033[m \033[31m{:.2f}'.format(dp + kp))
# errei no tipo primitivo do km que era float e não int
