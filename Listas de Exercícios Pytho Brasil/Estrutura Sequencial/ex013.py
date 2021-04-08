h = float(input('Informe a altura: '))

peso_ideal_homem = (72.7 * h) - 58
peso_ideal_mulher = (62.1 * h) - 44.7

print(f'Peso ideal para homens: \033[1:97m{peso_ideal_homem:.2f}\033[m.')
print(f'Peso ideal para mulheres: \033[1:97m{peso_ideal_mulher:.2f}\033[m.')