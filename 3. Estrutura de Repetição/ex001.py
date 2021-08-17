"""
    Exercício 1

    Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

numero = float(input('Digite uma nota (Entre 0 e 10): '))

while numero < 0 or numero > 10:
    numero = float(input('Valor inválido.\nDigite novamente: '))

print(f'Nota {numero:.2f}.')
