"""
    Exercício 49

    Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m

Imprima no final a soma da série.
"""

soma = 0
a = b = cont = 1

termos = int(input('Número de termos: '))
print('S = ', end='')

while cont <= termos:
    if cont == termos:
        print(f'{a}/{b}')
    else:
        print(f'{a}/{b}', end=' + ')

    soma += a/b

    a += 1
    b += 2

    cont += 1

print(f'Soma dos termos: {soma:.2f}')
