"""
    Exercício 4

    Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere 'P', se seu argumento for positivo, 
e 'N', se seu argumento for zero ou negativo.
"""

valor = int(input('Digite um valor: '))

def status_numero(n):
    if n > 0:
        return 'P'
    else:
        return 'N'

print(status_numero(valor))
