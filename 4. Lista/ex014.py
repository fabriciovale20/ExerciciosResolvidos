"""
    Exercício 14

    Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?" 

    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

from time import sleep

informacoes = [["Telefonou para a vítima?"], ["Esteve no local do crime?"], ["Mora perto da vítima?"],
["Devia para a vítima?"], ["Já trabalhou com a vítima?"]]

cont = 0

print('-'*30)
print('INVESTIGAÇÃO DE CRIME'.center(30))
print('-'*30)

print('Responda as perguntas com Sim ou Não, vamos começar a investigação.')
print('Aguarde um momento', end='')
for c in range(0, 3):
    sleep(1)
    print('.', end='')
print('\n')

# Coletando respostas das perguntas realizadas
while cont < 5:
    try:
        resposta = str(input(f'{informacoes[cont][0]} ')).strip().upper()[0]
        if resposta in 'SN':
            informacoes[cont].append(resposta)
            cont += 1
        else:
            print('Resposta inválida, tente novamente.')
            continue
    except Exception:
        print('Resposta inválida, tente novamente.')
        continue

print('\nPerguntas finalizadas, consultando o resultado', end='')
for c in range(0, 3):
    sleep(1)
    print('.', end='')
print()

# Verificando respostas informadas SIM e NÃO para conseguirmos o resultado
participacao = 0
for dados in informacoes:
    if dados[1] == 'S':
        participacao += 1

resultado = ''
if participacao < 2:
    resultado = '\033[1;97mINOCENTE\033[m'
elif participacao == 2:
    resultado = '\033[1;96mSUSPEITO\033[m'
elif participacao > 2 and participacao < 5:
    resultado = '\033[1;93mCÚMPLICE\033[m'
else:
    resultado = '\033[1;91mASSASSINO\033[m'

print(f'Resultado: {resultado}')
