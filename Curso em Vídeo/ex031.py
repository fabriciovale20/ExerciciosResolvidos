#Custo da Viagem
km = int(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de \033[1:30m{km}Km\033[m.')
valor = 0
if km > 200:
    valor = km*0.45
    print(f'E o preço da sua passagem será de \033[34mR${valor:.2f}\033[m.')
else:
    valor = km*0.5
    print(f'E o preço da sua passagem será de \033[31mR${valor:.2f}\033[m.')