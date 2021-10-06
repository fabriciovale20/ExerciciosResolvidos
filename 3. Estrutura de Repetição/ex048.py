"""
    Exercício 48

    Faça um programa que peça um número inteiro positivo e em seguida mostre este número invertido.
Exemplo:
12376489 => 98467321
"""

while True:
    try:
        numero = int(input('Numero: '))
    except Exception:
        print('\033[91mERRO: Digite um número inteiro válido.\033[m')
        continue
    else:
        print('Número invertido: ', end='')
        numero = str(numero)
        print(numero[::-1])
        break
