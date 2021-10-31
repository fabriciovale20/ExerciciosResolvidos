"""
    Exercício 4

    Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

lista = list()
consoantes = list()

cont = 0

for c in range(1, 11):
    lista.append(str(input(f'{c}º letra: ')))

for letra in lista:
    if letra not in 'aeiou':
        cont += 1
        consoantes.append(letra)

print(f'\nForam digitadas {cont} consoantes: ', end='')
for cons in consoantes:
    print(cons, end=' ')