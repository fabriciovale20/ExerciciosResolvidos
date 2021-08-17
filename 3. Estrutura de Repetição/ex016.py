"""
    A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""

numero = 1
anterior = anterior_2 = 0
while numero < 500:
    if numero == 1:
        anterior = 2
        anterior_2 = 1
        print(f'0 {numero} {numero} {anterior}', end=' ')
    numero = anterior + anterior_2
    anterior_2 = anterior
    anterior = numero

    print(numero, end=' ')
