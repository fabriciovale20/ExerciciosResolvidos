"""
    Exercício 9

    Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

vetor_a = []

soma_dos_quadrados = 0

while True:
    try:
        numero = int(input(f'{len(vetor_a)+1}º número: '))
    except Exception:
        print('Valor inválido, tente novamente!')
        continue
    else:
        vetor_a.append(numero)
        soma_dos_quadrados += numero ** 2

        if len(vetor_a) == 10:
            break

print(f'Soma dos quadrados: {soma_dos_quadrados}')
