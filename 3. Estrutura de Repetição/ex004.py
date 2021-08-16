populacao_a = 80000
crescimento_a = 3

populacao_b = 200000
crescimento_b = 1.5

anos = 0

while populacao_a < populacao_b:
    populacao_a += (populacao_a * (crescimento_a/100))
    populacao_b += (populacao_b * (crescimento_b/100))
    anos += 1

print(f'São necessários {anos} anos para que a população fique com a mesma quantidade.')