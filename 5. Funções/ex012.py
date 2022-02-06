"""
    Exercício 12

    Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""

from random import randint

def embaralhas(palavra):
    num_letras = len(palavra) - 1 # Número de letras da palavra
    num_registrados = [] # Registrar índice das letras sorteadas
    palavra_embaralhada = [] # Lista gerada com as palavras sorteadas

    while len(num_registrados) <= num_letras: # Condição para rodar todas as letras da palavra
        num = randint(0, num_letras)

        if num not in num_registrados: # Só acrescentar a string das letras sorteadoas se o índice não for repetido
            palavra_embaralhada.append(palavra[num]) # Adiconando a lista que será gerada a palavra embaralhada
            num_registrados.append(num) # Lista dos índices já sorteados
        
    palavra_embaralhada = ''.join(palavra_embaralhada) # Convertendo Lista em String

    return palavra_embaralhada

while True:
    palavra = input('Digite uma palavra: ').strip().lower() # Strip para remover espaços descenessários e Lower para deixar a palavra minúscula
    if palavra == 'fim': # Defini um parâmetro para encerrar o programa
        print('Programa finalizado!')
        break

    print(embaralhas(palavra))
