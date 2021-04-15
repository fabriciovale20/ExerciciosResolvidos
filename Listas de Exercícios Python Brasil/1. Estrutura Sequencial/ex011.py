n1 = int(input('Primeiro valor (Inteiro): '))
n2 = int(input('Segundo valor (Inteiro): '))
n3 = float(input('Terceiro valor (Real): '))

print(f'O produto do dobro do primeiro com metade do segundo: \033[1:97m{2*n1*(n2/2)}\033[m.')
print(f'A soma do triplo do primeiro com o terceiro: \033[1:97m{3*n1 + n3}\033[m.')
print(f'O terceiro elevado ao cubo: \033[1:97m{n3**3}\033[m.')