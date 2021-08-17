"""
    Exercício 20

    Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançadpa
or aluno e presentar:

a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c) A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
nota_3 = float(input('Terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3

# A mensagem "Aprovado com Distinção", se a média for igual a 10.
if media == 10:
    print(f'Aprovado com Distinção com média {media}')
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
elif media >= 7:
    print(f'Aprovado com média {media}')
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
elif media < 7:
    print(f'Reprovado com média {media}')
