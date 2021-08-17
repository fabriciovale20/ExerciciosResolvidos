"""
    Exercício 39

    Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e
o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

for c in range(1,11):
    print(f'{c}º Aluno')
    altura = float(input('Altura: '))
    if c == 1:
        aluno_alto = c
        altura_maior = altura
        aluno_baixo = c
        altura_menor = altura
    if altura > altura_maior:
        aluno_alto = c
        altura_maior = altura
    elif altura < altura_menor:
        aluno_baixo = c
        altura_menor = altura

print(f'Aluno {aluno_alto} é o mais alto com {altura_maior} metros.')
print(f'Aluno {aluno_baixo} é o mais alto com {altura_menor} metros.')
