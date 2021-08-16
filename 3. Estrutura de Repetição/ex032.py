numero = int(input('Fatorial de: '))
print(f'{numero}! = ', end = '')
fatorial = 1
for c in range(numero,0,-1):
    fatorial *= c
    if c == 1:
        print(f'1 = {fatorial}')
    else:
        print(c, end= ' . ')