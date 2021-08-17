"""
    Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
intervalo compreendido por eles.
"""

valor_a = int(input('Primero número: '))
valor_b = int(input('Segundo número: '))

if valor_a > valor_b:
    for c in range(valor_a-1, valor_b, -1):
        print(c,end=' ')
elif valor_b > valor_a:
    for c in range(valor_a+1, valor_b):
        print(c,end=' ')
