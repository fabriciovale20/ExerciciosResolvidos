n = int(input('Digite um valor: '))
cont = 0

for c in range(1, n+1):
    if n % c == 0:
        cont += 1

print(f'O número informado {n} ', end="")

if cont == 2:
    print('é primo.')
else:
    print('não é primo.')