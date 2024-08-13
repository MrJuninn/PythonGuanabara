print('\033[35mIMC\033[m')
print('\033[35m-\033[m'*3)
peso = float(input('Qual o seu peso? (Kg):'))
altura = float(input('Qual a sua altura?:(m)'))
imc = peso / altura ** 2
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[35mabaixo do peso\033[m')
elif imc > 18.5 and imc <= 25:
    print('Você está com o \033[35mpeso ideal\033[m')
elif imc > 25 and imc <= 30:
    print('Você está com \033[35msobrepeso\033[m')
elif imc > 30 and imc <= 40:
    print('Você está com \033[35mobesidade\033[m')
else:
    print('Você está com \033[35mobesidade mórbida\033[m')
