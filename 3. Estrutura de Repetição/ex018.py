"""
    Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

numero = cont = 0

while True:
    cont += 1
    numero = int(input(f'{cont}º número (Parar digite 9999): '))
    if numero == 9999:
        break
    elif cont == 1:
        menor = numero
        maior = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f'Número digitados {cont}\nMaior: {maior}\nMenor: {menor}')
