exp = []
exp.append(str(input('Escreva uma expressão: ')))
if exp[0].count('(') == exp[0].count(')'):
    print('Sua expressão está certa!')
else:
    print('Sua expressão está errada!')
