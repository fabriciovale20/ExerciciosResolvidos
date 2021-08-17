"""
    Um posto está vendendo combustíveis com a seguinte tabela de descontos:

a) Álcool:
b) até 20 litros, desconto de 3% por litro
c) acima de 20 litros, desconto de 5% por litro

d) Gasolina:
e) até 20 litros, desconto de 4% por litro
f) acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo
cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

combustivel = input('Gasolina ou Álcool (G / A)? ')
litros = int(input('Quantidade de litros? '))

print()

# Álcool até 20 litros, desconto de 3% por litro / acima de 20 litros, desconto de 5% por litro (R$ 1,90)
if combustivel == 'A':
    preco = 1.9
    combustivel = 'Álcool'
    if litros > 20:
        desconto = 5
    else:
        desconto = 3

# Gasolina até 20 litros, desconto de 4% por litro/ acima de 20 litros, desconto de 6% por litro (R$ 2,50)
elif combustivel == 'G':
    preco = 2.5
    combustivel = 'Gasolina'
    if litros > 20:
        desconto = 6
    else:
        desconto = 4

valor_combustivel = preco * litros
valor_desconto = desconto/100
total = valor_combustivel - (valor_combustivel * valor_desconto)

print(f'Combustível escolhido: {combustivel}\n'
      f'Valor: R$ {preco:.2f}\n'
      f'Litros: {litros}\n'
      f'Desconto: {desconto}%\n'
      f'Valor total à pagar: R$ {total:.2f}')
