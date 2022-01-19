"""
    Exercício 9

    Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
Por exemplo: 127 -> 721.
"""

def reverso_numero(n):
    n = str(n)
    n_invertido = n[::-1]
    
    return n_invertido

while True:
    try:
        numero = int(input('Digite um número inteiro: '))
    except Exception:
        print('Número inválido, tente novamente.')
    else:
        print(f'Número invertido {reverso_numero(numero)}.')
        break
