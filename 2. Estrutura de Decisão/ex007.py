"""
    Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n1
elif n3 > n1 and n3 > n2:
    maior = n3
    if n2 > n1:
        menor = n1
    else:
        menor = n2

print(f'O maior valor é {maior} e menor {menor}')
