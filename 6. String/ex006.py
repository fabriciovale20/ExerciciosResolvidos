"""
    Exercício 5

    Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""

data = input('Data de Nascimento: ')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

if len(data) != 10:
    print('Data inválida')
else:
    if mes == 1:
        mes_string = 'Janeiro'
    elif mes == 2:
        mes_string = 'Fevereiro'
    elif mes == 3:
        mes_string = 'Março'
    elif mes == 4:
        mes_string = 'Abril'
    elif mes == 5:
        mes_string = 'Maio'
    elif mes == 6:
        mes_string = 'Junho'
    elif mes == 7:
        mes_string = 'Julho'
    elif mes == 8:
        mes_string = 'Agosto'
    elif mes == 9:
        mes_string = 'Setembro'
    elif mes == 10:
        mes_string = 'Outubro'
    elif mes == 11:
        mes_string = 'Novembro'
    elif mes == 12:
        mes_string = 'Dezembro'

    print(f'Você nasceu em {dia} de {mes_string} de {ano}.')
    