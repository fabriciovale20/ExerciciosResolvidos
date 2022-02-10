"""
    Exercício 4

    Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

nome = input('Digite seu nome: ').strip().upper()

# OPÇÃO 1
n = ''
for c in nome:
    n += c
    print(n)

# OPÇÃO 2
# for c in range(len(nome)+1):
#     print(nome[:c])

