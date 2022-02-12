"""
    Exercício 10

    Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
"""

num_dct = {1: 'Um', 2: 'Dois', 3: 'Três', 4: 'Quatro', 5: 'Cinco', 6: 'Seis', 7: 'Sete', 8: 'Oito', 9: 'Nove', 10: 'Dez', 11: 'Onze',
12: 'Doze', 13: 'Treze', 14: 'Quatorze', 15: 'Quinze', 16: 'Dezesseis', 17: 'Dezessete', 18: 'Dezoito', 19: 'Dezenove', 20: 'Vinte',
30: 'Trinta', 40: 'Quarenta', 50: 'Cinquenta', 60: 'Sessenta', 70: 'Setenta', 80: 'Oitenta', 90: 'Noventa'}

num = int(input('Infomr um número (1 à 99): '))

if 1 > num > 99:
    print('Informe um valor entre 1 e 99.')
else:
    if num <= 20:
        print(num_dct[num])
    else:
        dezena = (num // 10) * 10 # // é o ÍNDICE da divisão (Por exemplo: 52 dividido por 10, o índice será 5, em seguida multiplico por 10)
        unidade = num % 10 # % é o RESTO da divisão (Por exemplo: 52 divido por 10, o resto será 2)

        print(f'{num_dct[dezena]} e {num_dct[unidade]}')


