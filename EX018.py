import math
# Ler un angulo e dizer o valor de seno, cosseno e tangente
print('\033[35m=\033[m'*11)
print('\033[31mCalculadora\033[m')
print('\033[35m=\033[m'*11)
angulo = float(input('\033[33mDigite um angulo:\033[m'))
s = math.radians(angulo)
c = math.radians(angulo)
t = math.radians(angulo)
print ('O ângulo \033[31m{:.0f}\033[m em Seno \033[35m{:.2f}\033[m \nO ângulo \033[31m{:.0f}\033[m em Cosseno \033[35m{:.2f}\033[m \nO ângulo \033[31m{:.0f}\033[m em Tangente \033[35m{:.2f}\033[m'.format(angulo, math.sin(s), angulo, math.cos(c), angulo, math.tan(t)))
# Eu errei em tudo pois eu não procurei direito e não converti da maneira correta, pois tem que pegar o valor do angulo em radianos e converter para seno, cosseno e tangente
