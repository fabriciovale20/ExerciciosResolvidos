numero = int(input('Digite um número: '))

cont = 0

for c in range(1, numero+1):
    if numero % c == 0:
        cont += 1
if cont == 2:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.\n'
          f'Números que são divisíveis: ', end='')
    for c in range(1, numero+1):
        if numero % c == 0:
            print(c, end = ' ')
