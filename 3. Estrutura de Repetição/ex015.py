"""
    A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

termo = int(input('Número de termos: '))

numero = 1
anterior = anterior_2 = 0

for c in range(1, termo+1):
    if numero == 1 and c == 1:
        anterior = 2
        anterior_2 = 1
        print(f'{numero} {c} {anterior}', end=' ')
    numero = anterior + anterior_2
    anterior_2 = anterior
    anterior = numero

    print(numero, end=' ')
