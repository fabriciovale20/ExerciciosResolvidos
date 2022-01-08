"""
    Exercício 3

    Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

def soma(a, b, c):
    print(a + b + c)

soma(n1, n2, n3)