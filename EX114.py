import urllib
import urllib.request

try:
    site = urllib.request.urlopen('Http://www.pudim.com.br')
except:
    print('O site Pudim não está acessivel no momento.')
else:
    print('Consegui acessar o site pudim com sucesso!')
