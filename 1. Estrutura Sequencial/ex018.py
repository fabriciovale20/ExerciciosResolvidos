"""
    Exercício 18

    Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

from math import ceil

tamanho = int(input('Tamanho do Arquivo em MB: '))
velocidade = int(input('Velocidade do Link: '))

tempo = ceil(tamanho/(velocidade/8))

print(f'{tempo} segundos')
