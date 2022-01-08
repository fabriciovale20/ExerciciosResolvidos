"""
    Exercício 17

    Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

from time import sleep

dados = [[], []]

while True:
    nome = str(input('Nome do atleta: '))
    if nome == '':
        break
    else:
        dados[0].append(nome)

    print('SALTOS')

    cont = 1

    while cont <= 5:
        try:
            salto = float(input(f'{cont}º salto: '))
        except Exception:
            print('Valor inválido, tente novamente.')
            continue
        else:
            cont += 1
            dados[1].append(salto)

    print('\nSaltos coletados, gerando resultado', end='')
    for c in range(3):
        sleep(0.5)
        print('.', end='')

    print()
    print('-'*20)
    print('RESULTADO'.center(20))
    print('-'*20)
    print(f'Atleta: {nome}\n')
    print(f'''
Primeiro Salto: {dados[1][0]} m
Segundo Salto: {dados[1][1]} m
Terceiro Salto: {dados[1][2]} m
Quarto Salto: {dados[1][3]} m
Quinto Salto: {dados[1][4]} m\n''')

    print(f'''
Resultado final:
Atleta: {nome}
Saltos: ''', end='')
    n = 0
    soma_saltos = 0
    for saltos in dados[1]:
        n += 1
        soma_saltos += saltos
        if n == 5:
            print(saltos)
        else:
            print(saltos, end=' - ')

    print(f'Média dos saltos: {soma_saltos / 5:.1f} m')
    
    dados = [[], []]
    cont = 0

    print('-'*30)
    print()

print('Programa finalizado!')