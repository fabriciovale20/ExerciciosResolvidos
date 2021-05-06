print('Lojas Tabajara')

total = n = 0

while True:
    n += 1
    preco = float(input(f'Produto {n}: R$ '))
    total += preco
    if preco == 0 and total == 0:
        print('Caixa finalizado, programa encerreado.')
        break
    elif preco == 0:
        print(f'Total: R$ {total:.2f}')
        dinheiro = float(input('Dinheiro: R$ '))
        print(f'Troco: R$ {dinheiro - total:.2f}')
        print('-'*20)
        print('Lojas Tabajaras')
        n = 0
        total = 0