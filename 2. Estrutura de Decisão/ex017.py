"""
    Exercício 17

    Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano
é ou não bissexto.
"""

ano = int(input('Informe o ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} \033[1:32mÉ BISSESXTO\033[m')
else:
    print(f'O ano {ano} \033[1:31mNÃO É BISSEXTO\033[m')
