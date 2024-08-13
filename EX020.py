from random import shuffle
a1 = str(input('Primeiro Aluno:'))
a2 = str(input('Segundo Aluno:'))
a3 = str(input('Terceiro Aluno:'))
a4 = str(input('Quarto Aluno:'))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(lista)
# O shuffle so funcionou em uma linha separada para ele embaralhar
# e a lista foi em colchetes, estudar sobre isso(estudei testando e não funciona com parenteses e sim com colchete)
