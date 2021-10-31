"""
    Exercício 2

    Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista = list()

print('---- Digite 10 números reais ----')
for c in range(1, 11):
    lista.append(float(input(f'{c} número: ')))

print('\nNúmeros digitados: ', end='')
for num in range(len(lista)-1, -1, -1):
    print(lista[num], end=' ')
