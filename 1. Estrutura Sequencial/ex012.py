"""
    Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58.
"""

altura = float(input('Informe a altura: '))

peso_ideal = (72.7 * altura) - 58

print(f'Peso Ideal: \033[1:97m{peso_ideal}\033[m.')
