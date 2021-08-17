"""
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

valor = float(input('Quando ganha por hora? R$'))
hora = int(input('Quantas horas trabalhou no mês? '))

salario = valor*hora

print(f'Você ganhou R${salario:.2f} no mês.')
