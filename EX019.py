import random
print('SORTEIO ALUNO')
a1 = str(input('\033[31mPrimeiro aluno:\033[m'))
a2 = str(input('\033[32mSegundo aluno:\033[m'))
a3 = str(input('\033[33mTerceiro aluno:\033[m'))
a4 = str(input('\033[34mQuarto aluno:\033[m'))
alunos = [a1, a2, a3, a4]
print('O aluno escolhido foi \033[35m{}\033[m'.format(random.choice(alunos)))
# Guanabara usou colchetes "[]" no "alunos" pois no python uma lista é com colchetes
