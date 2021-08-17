"""
    Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize
uma função de arredondamento.
"""

from math import ceil

n = float(input('Digite um número: '))

if n - ceil(n) != 0:
    print(f'O número {n} é decimal.')
else:
    print(f'O número {n} é inteiro')
