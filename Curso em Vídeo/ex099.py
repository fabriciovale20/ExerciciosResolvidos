from time import sleep

def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    sleep(1.0)
    maior = 0
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if valor > maior:
            maior = valor
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    sleep(1.0)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
