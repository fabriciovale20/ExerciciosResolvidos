"""
    Exercício 2

    Faça um programa para imprimir:

1
1 2
1 2 3
.......
1 2 3 .... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""

numero_termos = int(input('Digite um número: '))

def termos(n):
    for c in range(1, n+1):
        print(c, end=' ')

termos(numero_termos)
