"""
    Exercício 32

    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""

numero = int(input('Fatorial de: '))
print(f'{numero}! = ', end = '')
fatorial = 1
for c in range(numero,0,-1):
    fatorial *= c
    if c == 1:
        print(f'1 = {fatorial}')
    else:
        print(c, end= ' . ')
