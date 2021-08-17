"""
    Exercício 9

    Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

print('Ordem descrescente dos números ', end='')

if n1 > n2 and n1 > n3:
    p = n1
    if n2 > n3:
        s = n2
        t = n3
    else:
        s = n3
        t = n2
elif n2 > n1 and n2 > n3:
    p = n2
    if n1 > n3:
        s = n1
        t = n3
    else:
        s = n3
        t = n1
elif n3 > n1 and n3 > n2:
    p = n3
    if n1 > n2:
        s = n1
        t = n2
    else:
        s = n2
        t = n1

print(f'{p} - {s} - {t}')
