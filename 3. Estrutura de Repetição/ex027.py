"""
    Exercício 27

    Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e
a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""

turmas = int(input('Digite o número de turmas: '))

print()
print('Informe o número de alunos por turma.')

soma_alunos = 0

for c in range(1, turmas+1):
    alunos = int(input(f'{c}º turma: '))
    while alunos > 40:
        print('Número de alunos acima do permitido.')
        alunos = int(input(f'Tente novamente, {c}º turma: '))
    soma_alunos += alunos
    if c == 1:
        maior = alunos
        menor = alunos
        maior_turma = c
        menor_turma = c
    elif alunos > maior:
        maior = alunos
        maior_turma = c
    elif alunos < menor:
        menor = alunos
        menor_turma = c

print()
print(f'Turmas: {turmas}\n'
      f'Alunos: {soma_alunos}\n'
      f'\n'
      f'Maior {maior_turma}º turma com {maior} alunos.\n'
      f'Menor {menor_turma}º turma com {menor} alunos.\n'
      f'Média de {soma_alunos/turmas} alunos por turma.')
