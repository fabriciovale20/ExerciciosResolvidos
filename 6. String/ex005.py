"""
    Exercício 5

    Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""

nome = input('Digite seu nome: ').strip().upper()

for c in range(len(nome), 0, -1):
    print(nome[0:c])
