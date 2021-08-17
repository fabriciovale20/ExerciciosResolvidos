"""
    Exercício 18

    Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

if 0 < dia <= 31 and 0 < mes <= 12:
    if mes == 2 and dia <= 29 and ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('Data válida!')
    elif 0 < dia <= 31 and mes != 2:
        print('Data válida!')
    else:
        print('Data inválida!')
else:
    print('Data inválida!')
