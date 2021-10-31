"""
    Exercício 7

    Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

vetor = list()
multiplicacao = 1

for num in range(1, 6):
    vetor.append(int(input(f'{num}º número: ')))

print(f'\nSoma: {sum(vetor)}')

print(f'Multiplicação: ', end='')
for c in vetor:
    multiplicacao *= c
print(multiplicacao)

print('Número digitados: ', end='')
for c in vetor:
    print(c, end=' ')
