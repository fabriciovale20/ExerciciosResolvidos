"""
    Exercício 16

    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total.
"""

from math import ceil

area_pintada = int(input('Área Pintada em metros: '))

tintas = ceil((area_pintada*3)/18)

print(f'São necessárias aproximada,emte {tintas} latas de tinta, totalizando R${tintas*80:.2f}.')
