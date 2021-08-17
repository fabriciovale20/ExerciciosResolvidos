"""
    Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

numero = int(input('Digite um número: '))

cont = 0

for c in range(1, numero+1):
    if numero % c == 0:
        cont += 1
if cont == 2:
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')
