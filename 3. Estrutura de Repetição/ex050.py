"""
    Exercício 50

    Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
Faça um programa que calcule o valor de H com N termos.
"""

soma = 0

termos = int(input('Número de termos: '))
a = b = cont = 1

while cont <= termos:
    if cont == termos:
        print(f'{a}/{b}')
    elif cont == 1:
        print(f'{a}', end=' + ')
    else:
        print(f'{a}/{b}', end=' + ')

    soma += a/b
    cont += 1
    b += 1

print(f'Soma dos termos: {soma:.2f}')
