"""
    Exercício 41

    Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas % Juros sobre o valor inicial da dívida
            1                           0
            3                           10
            6                           15
            9                           20
            12                          25

Exemplo de saída do programa:
Valor da Dívida  / Valor dos Juros / Quantidade de Parcelas / Valor da Parcela
R$ 1.000,00             0                       1               R$ 1.000,00
R$ 1.100,00             100                     3               R$   366,00
R$ 1.150,00             150                     6               R$   191,67
"""

juros = 0

valor_divida = float(input('Valor da dívida: '))

print(f'\033[97m{"Valor da Dívida"} \033[91m| \033[97m{"Valor dos Juros"} \033[91m| '
      f'\033[97m{"Quantidade de Parcelas"} \033[91m| \033[97m{"Valor da Parcela"}\033[m')
for c in range(0, 13, 3):
    if c == 0:
        c += 1
        juros = 1
    elif c == 3:
        juros = 1.1  # Juros de 10
    elif c == 6:
        juros = 1.15  # Juros de 15
    elif c == 9:
        juros = 1.20  # Juros de 20
    else:
        juros = 1.25  # Juros de 25

    valor_divida_mais_juros = valor_divida * juros
    valor_das_parcelas = valor_divida_mais_juros / c

    print(f'  R$ {valor_divida_mais_juros:<8.2f} {valor_divida_mais_juros - valor_divida:^25.0f} {c:^10} '
          f'{"R$ ":>15} {valor_das_parcelas:>7.2f}')
