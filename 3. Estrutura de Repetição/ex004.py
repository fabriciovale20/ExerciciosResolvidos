"""
    Exercício 4

    Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
"""

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
