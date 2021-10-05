"""
    Exercício 46

    Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultado são eliminados. O seu resultado fica sendo a média dos três valores restantes.
    Você deve fazer um programa qu receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a
média). Faça usp de uma lista para armazenar os saltos. Os saltos são informados na ordem de execução, portanto não são
ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa de ve ser
conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salt: 6.5 m
Segundo Salt: 6.1 m
Terceiro Salt: 6.2 m
Quarto Salt: 5.4 m
Quinto Salt: 5.3 m

Melhor Salto: 6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9

Resulta final:
Rodrigo Curvêllo: 5.9 m
"""

from time import sleep

atleta = ['']
saltos_lista = list()

while True:
    try:
        nome = str(input('\033[97mNome do atleta:\033[m ')).strip()
    except Exception:
        print('ERRO: Nome inválido, tente novamente.')
        continue
    else:
        if nome == '':
            print('\n\033[96mColetando informações', end='')
            for c in range(0, 3):
                sleep(1)
                print('.', end='')
            print('\033[m')
            break
        else:
            atleta[0] = nome
            saltos_lista.clear()

    cont = 1
    while cont <= 5:
        try:
            salto = float(input(f'{cont}º salto: '))
        except Exception:
            print('\033[91mERRO: Valor do salto inválido, tente novamente.\033[m')
            continue
        else:
            saltos_lista.append(salto)
            cont += 1
    print()

media_saltos = (sum(saltos_lista) - max(saltos_lista) - min(saltos_lista))/3

print('-'*30)
print('\033[93mRESULTADO FINAL\033[m'.center(40))
print('-'*30)
print(f'''Atleta: \033[97m{atleta[0]}\033[m

Primeiro Salto: {saltos_lista[0]} m
Segundo Salto: {saltos_lista[1]} m
Terceiro Salto: {saltos_lista[2]} m
Quarto Salto: {saltos_lista[3]} m
Quinto Salto: {saltos_lista[4]} m

Melhor salto: {max(saltos_lista)} m
Pior salto: {min(saltos_lista)} m
Média dos demais saltos: {media_saltos:.1f} m

\033[97mResultado final:
{atleta[0]}: {media_saltos:.1f} m''')
