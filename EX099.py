from time import sleep

def maior(* nums):
    cont = mai = 0
    print('-=' * 28)
    print('Analisando os valores passados...')
    for c in nums:
        cont += 1
        print(f'{c} ', end='')
        sleep(0.5)
        if c > mai:
            mai = c
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')



# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
