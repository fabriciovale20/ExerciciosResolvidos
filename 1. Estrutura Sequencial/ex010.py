"""
    Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

temperatura = int(input('Informe a temperatura em Celsius: '))

fahrenheit = (temperatura * (9/5)) + 32

print(f'Temperatura em Fahrenheit {fahrenheit:.2f}ºF.')
