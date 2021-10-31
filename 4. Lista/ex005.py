"""
    Exercício 5

    Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

vetor = list()
par = list()
impar = list()

for c in range(1, 21):
    vetor.append(int(input(f'{c}º número: ')))

for numero in vetor:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'\n\033[97mNúmero digitados: ', end='')
for c in vetor:
    print(c, end=' ')

print(f'\n\033[mPar: ', end='')
for pares in par:
    print(pares, end=' ')

print(f'\nÍmpar: ', end='')
for impares in impar:
    print(impares, end=' ')
