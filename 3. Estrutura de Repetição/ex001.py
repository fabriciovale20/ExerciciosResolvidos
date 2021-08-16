numero = float(input('Digite uma nota (Entre 0 e 10): '))

while numero < 0 or numero > 10:
    numero = float(input('Valor inválido.\nDigite novamente: '))

print(f'Nota {numero:.2f}.')