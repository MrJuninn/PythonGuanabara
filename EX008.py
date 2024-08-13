print('=========')
print('Conversor')
print('=========')
N = float(input('Digite o valor a ser convertido(m):'))
c = N * 100
m = N * 1000
km = N / 1000
hm = N / 100    
dam = N / 10
dm = N * 10
print('{} metros é: \n\033[35m{}\033[m KM \n\033[35m{}\033[m HM \n\033[35m{}\033[m DAM \n\033[35m{}\033[m DM \n\033[35m{}\033[m CM \n\033[35m{}\033[m MM'.format(N, km, hm, dam, dm, c, m))
# Km, Hm, Dam, Dm, Cm, Mm
