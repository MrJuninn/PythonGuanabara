def voto(y=0):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - y
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos:  VOTO OBRIGATÓRIO.'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
