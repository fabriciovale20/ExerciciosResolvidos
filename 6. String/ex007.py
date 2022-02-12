"""
    Exercício 7

    Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

a) Quantos espaços em branco existem na frase.
b) Quantas vezes aparecem as vogais a, e, i, o, u.
"""

palavra = input('Digite a palavra: ')

print(f'a) Quantos espaços em branco existem na frase: {palavra.count(" ")}')
print(f'''b) Quantas vezes apaecem as vogais a, e, i, o, u.
a: {palavra.count('a')} | e: {palavra.count('e')} | i: {palavra.count('i')} | o: {palavra.count('o')} | u: {palavra.count('u')}''')
