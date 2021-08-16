numero = int(input('Digite um número (Entre 1 e 10): '))

print(f'Tabuada de {numero}:')
for c in range(1, 11):
    print(f'{numero} x {c} = {numero * c}')
