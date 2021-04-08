valor = float(input('Quanto ganha por hora? R$'))
hora = int(input('Quantas horas trabalhadas? '))

salario_bruto = valor * hora
print(f'+ Salário Bruto : R${salario_bruto:.2f}')

ir = salario_bruto*0.11
print(f'- IR (11%) : R${ir:.2f}')

inss = salario_bruto*0.08
print(f'- INSS (8%) : R${inss:.2f}')

sindicato = salario_bruto*0.05
print(f'- Sindicato (5%) : R${sindicato:.2f}')

descontos = ir + inss + sindicato

salario_liquido = salario_bruto - descontos
print(f'= Salário Líquido : R${salario_liquido:.2f}')
