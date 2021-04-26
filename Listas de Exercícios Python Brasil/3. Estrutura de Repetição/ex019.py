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