"""
    Exercício 1

    Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

lista = []

for c in range(1, 6):
    lista.append(int(input(f'Digite o {c}º número: ')))

print('Número digitados: ', end='')
for num in lista:
    print(num, end=' ')
