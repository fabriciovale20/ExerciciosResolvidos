"""
    Exercício 47

    Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior são eliminadas.
A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média conforme a descrição acima
informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são
informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9.04
"""

from time import sleep

print('-'*30)
print('NOTAS DO ATLETA'.center(30))
print('-'*30)

maior_nota = menor_nota = soma_nota = cont = 0

nome = str(input('\033[97mNome do atleta: \033[m'))

print('-'*30)
print(f'\033[97mAtleta: {nome}\033[m')

while cont < 7:
    try:
        nota = float(input('Nota: '))
    except Exception:
        print('\033[91mERRO: Nota inválida, tente novamente.\033[m')
        continue
    else:
        if cont == 0:
            maior_nota = menor_nota = nota
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota

        soma_nota += nota

        cont += 1

media_nota = (soma_nota - (maior_nota + menor_nota)) / 5

print('\nGerando notas', end='')
for c in range(0, 3):
    sleep(1)
    print('.', end='')
print()

print(f'''
Resultado final:
Atleta: {nome}
Melhor nota: {maior_nota}
Pior nota: {menor_nota}
Média: {media_nota:.2f}''')
