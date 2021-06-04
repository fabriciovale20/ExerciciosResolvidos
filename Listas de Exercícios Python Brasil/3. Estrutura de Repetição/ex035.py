n = int(input('Digite um valor: '))
numeros_primos = []

for a in range(1, n+1):
    cont = 0
    for b in range(1, a+1):
        if a % b == 0:
            cont += 1
    if cont == 2:
        numeros_primos.append(a)

print(f'Os números primos encontrados de 1 à {n} foram: ', end='')
for c in range(0, len(numeros_primos)):
    print(numeros_primos[c], end=' ')
