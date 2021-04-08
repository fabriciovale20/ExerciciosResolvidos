#Pintando parade
print('----PINTAR PAREDE-----')
largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
área = largura*altura
tinta = área/2
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de \033[1:30m{área:.2f}m²\033[m.')
print(f'Para pintar essa parede, você precisará de \033[1:34m{tinta:.2f}L\033[m de tinta.')
