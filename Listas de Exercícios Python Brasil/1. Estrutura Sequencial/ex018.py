from math import ceil

tamanho = int(input('Tamanho do Arquivo em MB: '))
velocidade = int(input('Velocidade do Link: '))

tempo = ceil(tamanho/(velocidade/8))

print(f'{tempo} segundos')