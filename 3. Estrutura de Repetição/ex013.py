"""
    Exercício 13

    Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
elevado ao segundo número. Não utilize a função de potência da linguagem.
"""

from math import pow

base = int(input('Digite um número (Base): '))
expoente = int(input('Digite uma número (Expoente): '))

print(f'Base {base}\nExpoente {expoente}\nResultado {pow(base,expoente):.2f}')
