"""
    Exercício 42

    Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número
negativo.
"""

numeros_0_25 = numeros_26_50 = numeros_51_75 = numeros_76_100 = 0

while True:
    while True:
        try:
            numero = int(input('Digite um valor: '))
        except Exception:
            print('\033[91mERRO: Valor inválido\033[m')
        else:
            break

    if numero < 0:
        break
    elif 0 <= numero <= 25:
        numeros_0_25 += 1
    elif 26 <= numero <= 50:
        numeros_26_50 += 1
    elif 51 <= numero <= 75:
        numeros_51_75 += 1
    else:
        numeros_76_100 += 1

print(f'''\n\033[97mRESULTADO, foram registrados:\033[m
- {numeros_0_25} número(s) entre [0-25]. 
- {numeros_26_50} número(s) entre [26-50].
- {numeros_51_75} número(s) entre [51-75].
- {numeros_76_100} número(s) entre [76-100].''')
