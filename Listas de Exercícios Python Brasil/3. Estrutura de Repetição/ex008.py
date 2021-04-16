soma = 0

for c in range (1, 6):
    numero = float(input(f'{c}º nota: '))
    soma += numero

print(f'Soma: {soma:.0f }\nMédia: {soma/5:.2f}')