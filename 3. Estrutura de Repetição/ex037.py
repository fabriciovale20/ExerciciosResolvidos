"""
    Exercício 37

    Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e
o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo,
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""

cont = soma_altura = soma_peso = 0

while True:
    cod = int(input('Código:'))
    if cod == 0:
        break
    altura = float(input('Altura (m): '))
    peso = float(input('Peso (Kg): '))

    soma_altura += altura
    soma_peso += peso

    cont += 1

    if cont == 1:
        maior_altura = altura
        maior_peso = peso
        maior_cod_altura = cod
        maior_cod_peso = cod
        menor_altura = altura
        menor_peso = peso
        menor_cod_altura = cod
        menor_cod_peso = cod

    if altura > maior_altura:
        maior_altura = altura
        maior_cod_altura = cod
    if altura < menor_altura:
        menor_altura = altura
        menor_cod_altura = cod

    if peso > maior_peso:
        maior_peso = peso
        maior_cod_peso = cod
    if peso < menor_peso:
        menor_peso = peso
        menor_cod_peso = cod

print()
print(f'Cadastros {cont}')
print(f'Mais alto {maior_altura:.2f} cm (Código {maior_cod_altura:.2f} / '
      f'Mais baixo {menor_altura:.2f} cm (Código {menor_cod_altura:.2f})')
print(f'Mais gordo {maior_peso:.2f} Kg (Código {menor_cod_altura:.2f} / '
      f'Mais magro {menor_peso:.2f} Kg (Código {menor_cod_peso:.2f})')
print(f'Média Altura {soma_altura/cont:.2f}')
print(f'Média Peso {soma_peso/cont:.2f}')
