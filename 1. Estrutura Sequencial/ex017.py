"""
    Exercício 17

    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
→ comprar apenas latas de 18 litros;
→ comprar apenas galões de 3,6 litros;
→ misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

from math import ceil

area_pintada = int(input('Informe o tamanho da área pintada: '))

print('-'*40)
lata = ceil((area_pintada/6)/18)
print('Caso for comprar em LATAS')
print(f'Latas: {lata} - R$ {lata*80:.2f}')
print()
galao = ceil((area_pintada/6)/3.6)
print('Caso for comprar em GALÕES')
print(f'Galões: {galao} - R$ {galao*25:.2f}')
print()
total = ceil((area_pintada/6)+(area_pintada*0.01))
latas = galoes = 0
print(f'Total de Litros: {total}')
while total >= 18:
    total -= 18
    latas += 1
while total < 18 and total > 0:
    total -= 3.6
    galoes += 1
print(f'Será necessário:\nLatas: {latas} - R$ {latas*80:.2f}\nGalões: {galoes} - R$ {galoes*25:.2f}\n\033[1:97mTotalizando: R$ {(latas*80)+(galoes*25):.2f}\033[m')
print('-'*40)
