"""
    Exercício 4

    Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

soma = media = cont = 0
for n in range(0,4):
    nota = float(input(f'{n+1}º nota: '))
    soma += nota
    cont += 1

print()
media = soma/cont
print(f'A média do aluno: {media:.2f}')
