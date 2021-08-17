"""
    Faça um Programa que leia três números e mostre o maior deles.
"""

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

print('O maior valor é ',end='')

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
elif n3 > n1 and n3 > n2:
    print(n3)
elif n1 == n2 == n3:
    print('\033[1:97mVALORES IGUAIS\033[m')
