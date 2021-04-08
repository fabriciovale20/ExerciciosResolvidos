#Separando dígitos de um número
n = int(input('Informe um número: '))
print(f'Analisando o número {n}')
a = n // 1 % 10
b = n // 10 % 10
c = n // 100 % 10
d = n // 1000 % 10
print(f'Unidade: {a}')
print(f'Dezena: {b}')
print(f'Centena: {c}')
print(f'Milhar: {d}')

