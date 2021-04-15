populacao_a = int(input('População A: '))
crescimento_a = float(input('Crescimento A: '))

populacao_b = int(input('População B: '))
crescimento_b = float(input('Crescimento B: '))

anos = 0
if populacao_a > populacao_b:
    while populacao_a > populacao_b:
        populacao_a += (populacao_a * (crescimento_a/100))
        populacao_b += (populacao_b * (crescimento_b/100))
        anos += 1
else:
    while populacao_b > populacao_a:
        populacao_a += (populacao_a * (crescimento_a/100))
        populacao_b += (populacao_b * (crescimento_b/100))
        anos += 1

print(f'São necessários {anos} anos para que a população fique com a mesma quantidade.')