"""
    Exercício 6

    Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

media_notas = list()
cont = 0

for alunos in range(1, 11):
    soma_notas = 0

    nome_aluno = str(input(f'Nome do {alunos}º aluno: '))
    print(f'Informe as notas do Aluno \033[97m{nome_aluno}\033[m.')

    for notas in range(1, 5):
        soma_notas += float(input(f'{notas} nota: '))
    
    media = soma_notas / 4

    if media >= 7:
        cont += 1

    print()
    media_notas.append(media)

print(f'\n{cont} alunos tiraram notas maiores ou iguais a 7.')
print(f'Notas: ', end='')

for maior_7 in media_notas:
    if maior_7 >= 7:
        print(maior_7, end='  ')
