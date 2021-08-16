cont = 0

while cont != 5:
    numero = int(input(f'{cont+1}º valor: '))
    cont += 1
    if cont == 1:
        maior = numero
    elif numero > maior:
        maior = numero

print(f'O maior número digitado foi {maior}')