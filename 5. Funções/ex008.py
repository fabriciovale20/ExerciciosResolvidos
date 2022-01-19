"""
    Exercício 8

    Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""

def contar_numeros(n):
    n_str = str(n)

    return len(n_str)

while True:
    try:
        numero = int(input('Informe um número: '))
    except Exception:
        print('Número inválido, tente novamente.')
    else:
        print(f'\nO número informado contém {contar_numeros(numero)} dígitos.')
        break
