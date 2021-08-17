"""
    Exercício 19

    Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

cont = menor = maior = numero = 0

print('Para encerrar o programa digite "parar".')

while True:
    cont += 1
    try:
        numero = int(input(f'{cont}º número: '))
        if numero > 999 or numero == 0:
            break
        elif cont == 1:
            menor = numero
            maior = numero
        elif numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    except ValueError:
        print("Programa encerreado!")
        break
