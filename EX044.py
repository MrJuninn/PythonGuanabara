print('{:=^40}'.format(' JUNINS LOJAS '))
valor = float(input('\033[33mQual o valor do produto?:\033[m'))
print('''\033[36mQual a condição de pagamento?\033[m
\033[31m[1]\033[m \033[35mà vista Dinheiro/Cheque\033[m
\033[31m[2]\033[m \033[35mà vista no mcartão:5% de desconto\033[m
\033[31m[3]\033[m \033[35mem até 2x no cartão:preço normal\033[m
\033[31m[4]\033[m \033[35m3x ou mais no cartão:20% de juros\033[m''')
forma = int(input('Qual a forma de pagamento?:'))
if forma == 1:
    print('O produto vai custar R${:.2f}'.format(valor - valor * 10 / 100))
elif forma == 2:
    print('O produto vai custar R${:.2f}'.format(valor - valor * 5 / 100))
elif forma == 3:
    print('O produto custa R${:.2f} e será pago em duas parcelas de R${:.2f}'.format(valor, valor / 2))
elif forma == 4:
    parcela = int(input('Você deseja parcelar de quantas vezes?:'))
    if parcela == 3:
        print('O produto irá custar R${:.2f} e será pago em 3 parcelas de R${:.2f}'.format(valor + valor * 20 / 100, (valor + valor * 20 / 100) / 3))
    elif parcela > 3:
        print('O produto irá custar R${:.2f} e será pago em {} parcelas de R${:.2f}'.format(valor + valor * 20 / 100, parcela,(valor + valor * 20 / 100) / parcela))
else:
    print('\033[31mComando inválido\033[m')
