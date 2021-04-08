#Reajuste Salarial
salário = float(input('Qual é o salário do Funcionário? R$'))
aumento = salário+(salário*0.15)
print(f'Um funcionário que ganhava \033[1:30mR${salário}\033[m, com 15% de aumento, passa a receber \033[1:31mR${aumento:.2f}\033[m.')