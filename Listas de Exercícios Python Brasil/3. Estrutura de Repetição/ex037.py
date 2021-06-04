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
