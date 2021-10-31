"""
    Exercício 12

    Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""

dados = [[29, 1.67], [27, 1.64], [13, 1.54], [12, 1.54], [15, 1.42], [14, 1.41], [30, 1.78], [45, 1.72], [10, 1.47], [15, 1.34], 
[18, 1.96], [22, 1.89], [24, 1.78], [17, 1.45], [20, 1.72], [24, 1.78], [12, 1.56], [9, 1.35], [11, 1.33], [12, 1.45], [9, 1.25], [5, 1.32],
[17, 1.89], [56, 1.64], [60, 1.78], [75, 1.59], [43, 1.76], [40, 1.68], [26, 1.46], [33, 1.98]]

media_altura = cont = 0

for c in range(0, len(dados)):
    media_altura += dados[c][1]

media_altura /= len(dados)

for c in range(0, len(dados)):
    if dados[c][0] > 13 and dados[c][1] < media_altura:
        cont += 1

print(f'Há {cont} alunos com mais de 13 anos e que possuem altura inferior à média.')
