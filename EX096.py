def área(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area}M²')


largura = float(input('Largura(M):'))
comprimento = float(input('Comprimento(M):'))
área(largura, comprimento)
