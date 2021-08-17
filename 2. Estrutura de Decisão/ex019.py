"""
    Exercício 19

    Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.

Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

valor = int(input('Número menos que 1000: '))

if valor >= 1000:
    print('Valor informado inválido!')
else:
    valor = str(valor)
    if len(valor) == 3:
        if int(valor[0]) > 1:
            print(f'{valor[0]} centenas, ',end='')
        else:
            print(f'{valor[0]} centena, ',end='')
        if int(valor[1]) > 1:
            print(f'{valor[1]} dezenas e ', end='')
        else:
            print(f'{valor[1]} dezena e ', end='')
        if int(valor[2]) > 1:
            print(f'{valor[2]} unidades.')
        else:
            print(f'{valor[2]} unidade.')
    elif len(valor) == 2:
        if int(valor[0]) > 1:
            print(f'{valor[0]} dezenas e ', end='')
        else:
            print(f'{valor[0]} dezena e ', end='')
        if int(valor[1]) > 1:
            print(f'{valor[1]} unidades.')
        else:
            print(f'{valor[1]} unidade.')
    elif len(valor) == 1:
        if int(valor[0]) > 1:
            print(f'{valor[0]} unidades.')
        else:
            print(f'{valor[0]} unidade.')
