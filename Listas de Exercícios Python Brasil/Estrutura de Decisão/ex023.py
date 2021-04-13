from math import ceil

n = float(input('Digite um número: '))

if n - ceil(n) != 0:
    print(f'O número {n} é decimal.')
else:
    print(f'O número {n} é inteiro')