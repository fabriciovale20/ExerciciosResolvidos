"""
    Exercício 14

    Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números ímpares.
"""

par = impar = 0

for c in range(1, 11):
    numero = int(input(f'{c}º número: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Números pares: {par}\nNúmero ímpares: {impar}')
