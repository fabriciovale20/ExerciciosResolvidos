"""
    Exercício 11

    As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
→ salários até R$ 280,00 (incluindo) : aumento de 20%
→ salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
→ salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
→ salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
→ o salário antes do reajuste;
→ o percentual de aumento aplicado;
→ o valor do aumento;
→ o novo salário, após o aumento.
"""

salario = float(input('Informe o salário: '))

if salario <= 280:
    aumento = 20
elif salario > 280 and salario <= 700:
    aumento = 15
elif salario > 700 and salario < 1500:
    aumento = 10
elif salario >= 1500:
    aumento = 5

print('-'*40)
print(f'Salário antes do reajuste: R$ {salario:.2f}')

print(f'Percentual de aumento aplicado: {aumento} %')

print(f'Valor do aumento: R$ {salario*(aumento/100):.2f}')

print(f'Novo salário, após o aumento: R$ {salario + (salario*(aumento/100)):.2f}')
