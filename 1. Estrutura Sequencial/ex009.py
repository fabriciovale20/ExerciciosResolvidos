"""
    Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)
"""

fahr = int(input('Informe a temperatura em Fahrenheit: '))

celsius = 5 * ((fahr-32) / 9)

print(f'Temperatura em Celsius {celsius:.2f}º.')
