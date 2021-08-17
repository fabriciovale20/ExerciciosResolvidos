"""
    Exercício 34

    Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
"""

n = int(input('Digite um valor: '))
cont = 0

for c in range(1, n+1):
    if n % c == 0:
        cont += 1

print(f'O número informado {n} ', end="")

if cont == 2:
    print('é primo.')
else:
    print('não é primo.')
