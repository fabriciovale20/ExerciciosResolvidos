"""
    Exercício 13

    Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

dados = [["1 - Janeiro"], ["2 - Fevereiro"], ["3 - Março"], ["4 - Abril"], ["5 - Maio"], ["6 - Junho"], ["7 - Julho"], ["8 - Agosto"], ["9 - Setembro"],
["10 - Outubro"], ["11 - Novembro"], ["12 - Dezembro"]]

soma_temperaturas = 0

print('-'*20)
print('TEMPERATURAS'.center(20))
print('-'*20)

for c in range(0, 12):
    dados[c].append(int(input(f"{dados[c][0]}: ")))

for c in dados:
    soma_temperaturas += c[1]

media = soma_temperaturas / 12

print(f'\nMédia anual das temperaturas: {media:.2f}')
print(f'\nTemperaturas acimda da média:')

for c in dados:
    if c[1] > media:
        print(c[0], end=' ')
        print(c[1])
