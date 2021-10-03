"""
    Exercício 44

    Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de um código.
Os códigos utilizados são:
1, 2, 3, 4 - Votos para os respectivos candidatos.
(Você deve montar a tabela ex: 1 - José / 2 - João / etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
• O total de votos para cada candidato;
• O total de votos nulos;
• O total de votos em branco;
• A percentagem de votos nulos sobre o total de votos;
• A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
"""

from time import sleep
from datetime import datetime

candidato_1 = candidato_2 = candidato_3 = candidato_4 = nulo = branco = 0
cont = 1

print('-'*30)
print(f'\033[1:97mELEIÇÕES {datetime.today().year}\033[m'.center(40))
print('-'*30)

print(f'''  \033[1:97mCandidato     \033[1:91m|\033[m   \033[1:97mCódigo\033[m
\033[96m    {"João":<13}{"1":>6}
    {"Pedro":<13}{"2":>6}
    {"Paula":<13}{"3":>6}
    {"Maria":<13}{"4":>6}
    {"Nulo":<13}{"5":>6}
    {"Branco":<13}{"6":>6}\033[m''')
print('-'*30)

print('\033[97mINICIANDO VOTAÇÃO (DIGITE 0 PARA FINALIZAR A VOTAÇÃO)\033[m')
print('Aguarde', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(0.7)
print('\n')

while True:
    try:
        voto = int(input(f'{cont}º voto: '))
        if voto < 0 or voto > 6:
            print(f'\033[93mAVISO: Voto inválido, tente novamente.\033[m')
            continue
    except Exception:
        print('\033[91mERRO: voto inválido, tente novamente.\033[m')
        continue
    else:
        if voto == 1:
            candidato_1 += 1
            print('Voto contabilizado para \033[97mJoão\033[m.\n')
        elif voto == 2:
            candidato_2 += 1
            print('Voto contabilizado para \033[97mPedro\033[m.\n')
        elif voto == 3:
            candidato_3 += 1
            print('Voto contabilizado para \033[97mPaula\033[m.\n')
        elif voto == 4:
            candidato_4 += 1
            print('Voto contabilizado para \033[97mMaria\033[m.\n')
        elif voto == 5:
            nulo += 1
            print('Voto contabilizado para \033[97mNulo\033[m.\n')
        elif voto == 6:
            branco += 1
            print('Voto contabilizado para \033[97mBranco\033[m.\n')
        else:
            print('-'*30)
            print('\033[1:93mVOTAÇÃO ENCERRADA\033[m'.center(40))
            print('-'*30)
            cont -= 1
            break

    cont += 1

print('\033[96mColetando dados da votação', end='')
for c in range(0, 3):
    sleep(1)
    print('.', end='')
print('\033[m')

print('-'*30)
print(f'''  \033[1:97mCandidato     \033[1:91m|\033[m   \033[1:97mVotos\033[m
\033[96m    {"João":<13}{candidato_1:>6}
    {"Pedro":<13}{candidato_2:>6}
    {"Paula":<13}{candidato_3:>6}
    {"Maria":<13}{candidato_4:>6}
    {"Nulo":<13}{nulo:>6}
    {"Branco":<13}{branco:>6}\033[m''')
print('-'*30)

print(f'\033[97mTOTAL DE VOTOS {cont}\033[m')
print(f'''\033[93m→ {(nulo*100)/cont:.1f}% Votos Nulos
→ {(branco*100)/cont:.1f}% Votos em Branco\033[m''')
