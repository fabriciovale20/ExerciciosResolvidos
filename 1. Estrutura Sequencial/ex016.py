from math import ceil

area_pintada = int(input('Área Pintada em metros: '))

tintas = ceil((area_pintada*3)/18)

print(f'São necessárias aproximada,emte {tintas} latas de tinta, totalizando R${tintas*80:.2f}.')