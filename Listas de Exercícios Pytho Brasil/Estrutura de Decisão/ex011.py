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