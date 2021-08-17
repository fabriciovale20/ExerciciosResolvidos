"""
    Exercício 25

    Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se
a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
conforme a média calculada.
"""

numero_de_pessoas = int(input('Número de pessoas: '))

cont = soma_idade = 0

for c in range(1, numero_de_pessoas+1):
    idade = int(input(f'Idade da {c}º pessoa: '))
    soma_idade += idade
    cont += 1
    if cont == 1:
        maior = idade
        menor = idade
    elif idade > maior:
        maior = idade
    elif idade < menor:
        menor = idade

media_idade = soma_idade/cont

if 0 < media_idade < 26:
    turma = 'Jovem'
elif 25 < media_idade < 61:
    turma = 'Adulta'
elif media_idade > 60:
    turma = 'Idosa'


print(f'Número de pessoas: {numero_de_pessoas}\n'
      f'Soma das idades: {soma_idade} (Maior idade: {maior} / Menor idade: {menor})\n'
      f'Média: {media_idade}\n'
      f'Classificação: {turma}')
