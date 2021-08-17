"""
    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

numero = int(input('Número para fatorar: '))

fatorial = 1

print(f'{numero}! = ', end='')
for c in range(numero, 0, -1):
    if c == 1:
        print(c, end=' = ')
    else:
        print(f'{c}.', end='')
    fatorial *= c
print(f'\033[97m{fatorial}\033[m')
