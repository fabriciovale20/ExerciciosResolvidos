# Nome: maior que 3 caracteres;
nome = input('Nome: ')
while len(nome) < 3:
    nome = input('Tente novamente, nome: ')

# Idade: entre 0 e 150;
idade = int(input('Idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Tente novamente, idade:'))

# Salário: maior que zero;
salario = float(input('Salário: R$ '))
while salario < 1:
    salario = float(input('Tente novamente, salário: '))

# Sexo: 'f' ou 'm';
sexo = input('Sexo (M/F): ').upper()
while sexo.upper() not in 'MF':
    sexo = input('Tente novamente, sexo: ').upper()
if sexo == 'F':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'

# Estado Civil: 's', 'c', 'v', 'd';
estado_civil = input('Estado civil (S/C/V/D): ').upper()
while estado_civil not in 'SCVD':
    estado_civil = input('Tente novamente, estado civil: ').upper()
if estado_civil == 'S':
    estado_civil = 'Solteiro(a)'
elif estado_civil == 'C':
    estado_civil = 'Casado(a)'
elif estado_civil == 'V':
    estado_civil = 'Viúvo(a)'
elif estado_civil == 'D':
    estado_civil = 'Divorciádo(a)'
print()

print(f'Nome: \033[96m{nome}\033[m\n'
      f'Idade: \033[96m{idade}\033[m\n'
      f'Sexo: \033[96m{sexo}\033[m\n'
      f'Salário: R$ \033[96m{salario:.2f}\033[m\n'
      f'Estado Civil: \033[96m{estado_civil}\033[m')