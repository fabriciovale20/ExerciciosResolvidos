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

