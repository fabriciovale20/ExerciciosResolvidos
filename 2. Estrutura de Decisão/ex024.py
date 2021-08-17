"""
    Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

a) par ou ímpar;
b) positivo ou negativo;
c) inteiro ou decimal.
"""

from math import ceil

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
print()
op = int(input('Qual operação deseja fazer:\n1- Soma\n2- Subtração\n3- Divisão\nEscolha: '))

if op == 1:
    resultado = n1 + n2
    operacao = 'soma'
elif op == 2:
    resultado = n1 - n2
    operacao = 'subtração'
elif op == 3:
    resultado = n1 / n2
    operacao = 'divisão'

if resultado - ceil(resultado):
    decimal = 'Sim'
else:
    decimal = 'Não'

if resultado >= 0:
    positivo_negativo = 'Positivo'
else:
    positivo_negativo = 'Negativo'

if resultado % 2 == 0:
    par_impar = 'Par'
else:
    par_impar = 'Ímpar'

print(f'A {operacao} entre {n1} e {n2} é igual a {resultado:.2f}.\n'
      f'O resultado é:\n'
      f'- Decimal? {decimal}\n'
      f'- Positivo ou negativo? {positivo_negativo}\n'
      f'- Par ou ímpar? {par_impar}')
