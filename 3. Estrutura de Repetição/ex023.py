"""
    Exercício 23

    Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

numero = int(input('Digite um número: '))
primos = list()
nao_primos = list()
divisoes = 0

for c in range(1, numero+1):
    cont = 0
    for n in range(1, c+1):
        if c % n == 0:
            cont += 1
        divisoes += 1
    if cont == 2:
        primos.append(c)
    else:
        nao_primos.append(c)
print(f'Foram realizadas {divisoes} divisões.')
print('Números primos: ', end='')
for c in primos:
    print(c, end=' ')
print()
print('Números não primos: ', end='')
for c in nao_primos:
    print(c, end=' ')
