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



