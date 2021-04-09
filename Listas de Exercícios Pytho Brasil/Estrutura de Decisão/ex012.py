valor = float(input('Informe o valor por hora: '))
hora = int(input('Horas trabalhadas: '))

salario = valor * hora

if salario <= 900:
    ir_percentual = 0
elif salario > 900 and salario <= 1500:
    ir_percentual = 5
elif salario > 1500 and salario <= 2500:
    ir_percentual = 10
elif salario > 2500:
    ir_percentual = 20

inss = salario * 0.1
fgts = salario * 0.11
ir = salario * (ir_percentual/100)

desconto = ir + inss
salario_liquido = salario - desconto

print(f"""
Salário Bruto: ({valor} * {hora})   : R$ {salario:.2f}
(-) IR ({ir_percentual}%)                  : R$ {ir:.2f}
(-) INSS (10%)               : R$ {inss:.2f}
FGTS (11%)                   : R$ {fgts:.2f}
Total de descontos           : R$ {desconto:.2f}
Salário Líquido              : R$ {salario_liquido:.2f}""")


