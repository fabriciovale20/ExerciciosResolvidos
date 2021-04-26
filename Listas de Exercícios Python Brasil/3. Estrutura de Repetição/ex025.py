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
