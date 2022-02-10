"""
    Exercício 1

    Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""

string_1 = input('Primeira string: ')
string_2 = input('Segunda string: ')

tamanho_1 = len(string_1)
tamanho_2 = len(string_2)

if tamanho_1 != tamanho_2: # Verificar se os tamanhos são iguais
    tamanho = 'diferentes'
    conteudo = 'diferente'
else:
    tamanho = 'iguais'
    if string_1 == string_2: # Verificando se o conteúdo é o mesmo
        conteudo = 'iguai'
    else:
        conteudo = 'diferente'

print(f'''String 1: {string_1}
String 2: {string_2}

Tamanho de {string_1}: {tamanho_1}
Tamanho de {string_2}: {tamanho_2}

As duas strings são de tamanhos {tamanho}
As duas strings possuem conteúdo {conteudo}''')
