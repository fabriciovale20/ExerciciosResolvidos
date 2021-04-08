#Calculando Descontos
valor = float(input('Qual é o preço do produto? R$'))
desconto = valor-(valor*0.05)
print(f'O produto que custava \033[1:30mR${valor}\033[m, na promoção com desconto de 5% vai custar \033[1:34mR${desconto:.2f}\033[m.')