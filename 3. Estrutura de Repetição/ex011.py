"""
    Exercício 11

    Altere o programa anterior para mostrar no final a soma dos números.
"""

valor_a = int(input('Primero número: '))
valor_b = int(input('Segundo número: '))

soma = 0

if valor_a > valor_b:
    for c in range(valor_a-1, valor_b, -1):
        print(c,end=' ')
        soma += c
elif valor_b > valor_a:
    for c in range(valor_a+1, valor_b):
        soma += c
        print(c,end=' ')

print()
print(f'Soma {soma}')
