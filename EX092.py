from datetime import datetime
ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
ficha['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if ficha['ctps'] == 0:
    print('-=' * 10)
    for c, i in ficha.items():
        print(f' - {c} tem o valor {i}')
else:
    ficha['contratação'] = int(input('Ano de Contratação: '))
    ficha['salario'] = float(input('Salário R$: '))
    ficha['aposentadoria'] = ficha['idade'] + (ficha['contratação'] + 35) - datetime.now().year
    print('-=' * 10)
    for c, i in ficha.items():
        print(f' - {c} tem o valor {i}')
