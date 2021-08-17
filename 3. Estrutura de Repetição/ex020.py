"""
    Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
limitando o fatorial a números inteiros positivos e menores que 16.
"""

print('Para encerrar o programa digite "Parar"!')
while True:
    fatorial_resultado = 1
    try:
        numero = int(input('Fatorial de: '))
        while numero < 1 or numero > 15:
            numero = int(input('Número inválido. Tente novamante, fatorial de: '))
        print(f'{numero}! = ', end='')
    except ValueError:
        print('Programa encerrado!')
        break
    for c in range(numero, 0, -1):
        if c == 1:
            print(f'{c} = ', end='')
        else:
            print(f'{c}', end='.')
        fatorial_resultado *= c
    print(fatorial_resultado)
