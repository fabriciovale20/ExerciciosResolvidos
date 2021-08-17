"""
    Exercício 8

    Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

produto1 = float(input('Primeiro produto R$'))
produto2 = float(input('Segundo produto R$'))
produto3 = float(input('Terceiro produto R$'))

print('Você deve comprar o produto de valor R$', end='')

if produto1 < produto2 and produto1 < produto3:
    print(produto1)
elif produto2 < produto1 and produto2 < produto3:
    print(produto2)
elif produto3 < produto1 and produto3 < produto2:
    print(produto3)
