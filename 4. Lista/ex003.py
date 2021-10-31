"""
    Exercício 3

    Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = list()

print('-'*20)
print('BOLETIM ALUNO'.center(20))
print('-'*20)

for c in range(1, 5):
    notas.append(float(input(f'{c}º nota: ')))

print(f'\nNotas informadas: ', end='')
for n in notas:
    print(n, end='  ')

print(f'\nMédia: {sum(notas) / len(notas)}')
