"""
    Exercício 14

    Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

          Média de Aproveitamento  Conceito
          Entre 9.0 e 10.0          A
          Entre 7.5 e 9.0           B
          Entre 6.0 e 7.5           C
          Entre 4.0 e 6.0           D
          Entre 4.0 e zero          E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1+n2)/2

print('-'*40)
print(f'Primeira nota {n1}')
print(f'Segunda nota {n2}')
print(f'Média {media}')
print('-'*40)
if 10 >= media >= 9:
    print('Conceito A, aprovado.')
elif 9 > media >= 7.5:
    print('Conceito B, aprovado.')
elif 7.5 > media >= 6:
    print('Conceito C, aprovado.')
elif 6 > media >= 4:
    print('Conceito D, reprovado.')
elif media > 4:
    print('Conceito E, reprovado.')
