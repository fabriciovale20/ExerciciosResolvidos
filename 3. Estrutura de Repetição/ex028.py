"""
    Exercício 28

    Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e
o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

numero_de_cds = int(input("Informe o número de CD's? "))

soma = cont = 0

while numero_de_cds > cont:
    cont += 1
    soma += int(input(f'Valor do {cont}º CD: R$'))

print()

print(f"\033[97mTotal de CD's {numero_de_cds}\033[m\n"
      f"Soma total: R$ {soma:.2f}\n"
      f"Custo médio por CD: R$ {soma/numero_de_cds:.2f}")
