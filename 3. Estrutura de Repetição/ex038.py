"""
    Exercício 38

    Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que
o usuário digite o salário inicial do funcionário.
"""

# Salário Inicial em 1995
salario_inicial = float(input('Salário Inicial R$ '))

# Aumento em 1996 de 1,5%
aumento = 1.5
salario_aumento = salario_inicial + (salario_inicial * (aumento/100))

# A partir de 1997 aumento do dobro do percentual do ano anterior
ano = 1996

for c in range(0, 24):
    aumento *= 2
    ano += 1
    salario_aumento += (salario_aumento * (aumento/100))
    print(f'Ano {ano} - Aumento de {aumento:.2f}%')
    print(f'R$ {salario_aumento:.2f}')
