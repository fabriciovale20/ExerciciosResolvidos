"""
    Exercício 3

    Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

F
U
L
A
N
O
"""

nome = input('Digite seu nome: ').strip().upper()

for c in nome:
    print(c)
