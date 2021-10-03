"""
    Exercício 45 ( Gabarito não definido )

    Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se o outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
a) Maior e menor acerto;
b) Total de alunos que utilizaram o sistema;
c) A média das notas da turma.

Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes
dos alunos usarem o programa.
"""

from time import sleep

maior_nota = menor_nota = media_pontos = total_de_alunos = soma_pontos = 0
aluno_maior_nota = aluno_menor_nota = ''
gabarito_1 = gabarito_2 = gabarito_3 = gabarito_4 = gabarito_5 = \
gabarito_6 = gabarito_7 = gabarito_8 = gabarito_9 = gabarito_10 = 0

print('-'*30)
print('\033[97mGABARITO\033[m'.center(35))
print('-'*30)

print('''\033[1:93mOlá Professor!!!
Por favor, preencha o gabarito das questões para iniciarmos as avaliações.\033[m''')
sleep(2)
print('\n\033[1:96m--- GABARITO ---\033[m')
for c in range(1, 11):
    while True:
        print(f'Questão {c} - ', end='')
        try:
            gabarito = str(input('')).strip().upper()
            if gabarito not in 'ABCDE' or gabarito == '':
                print('\033[93mAVISO: Alternativa inválida, tente novamente.\033[m')
                continue
        except Exception:
            print('\033[91mERRO: Resposta inválida.\033[m')
        else:
            if c == 1:
                gabarito_1 = gabarito
            elif c == 2:
                gabarito_2 = gabarito
            elif c == 3:
                gabarito_3 = gabarito
            elif c == 4:
                gabarito_4 = gabarito
            elif c == 5:
                gabarito_5 = gabarito
            elif c == 6:
                gabarito_6 = gabarito
            elif c == 7:
                gabarito_7 = gabarito
            elif c == 8:
                gabarito_8 = gabarito
            elif c == 9:
                gabarito_9 = gabarito
            else:
                gabarito_10 = gabarito
            break

print('-'*30)
print('\033[92mDefinindo gabarito\033[m', end='')
for i in range(0, 3):
    sleep(1)
    print('.', end='')
print('\033[m')

print('-'*30)
print('\033[97mAVALIAÇÃO FINAL\033[m'.center(35))
print('-'*30)

while True:
    total_pontos = 0

    aluno = str(input('\033[97mNome do aluno:\033[m ')).rstrip().lstrip().title()

    print(f'\n\033[1:93mBem-vindo(a), \033[1:97m{aluno}\033[m!')
    print('\033[1:93mA avaliação começará em instantes', end='')
    for i in range(0, 3):
        sleep(0.8)
        print('.', end='')
    print('\033[m')

    print('\n\033[1:96m--- AVALIAÇÃO INICIADA ---\033[m')

    for c in range(1, 11):
        while True:
            print(f'Questão {c} - ', end='')
            try:
                resp = str(input('')).strip().upper()
                if resp not in 'ABCDE' or resp == '':
                    print('\033[93mAVISO: Alternativa inválida, tente novamente.\033[m')
                    continue
            except Exception:
                print('\033[91mERRO: Resposta inválida.\033[m')
            else:
                if c == 1:
                    if resp == gabarito_1:
                        total_pontos += 1
                elif c == 2:
                    if resp == gabarito_2:
                        total_pontos += 1
                elif c == 3:
                    if resp == gabarito_3:
                        total_pontos += 1
                elif c == 4:
                    if resp == gabarito_4:
                        total_pontos += 1
                elif c == 5:
                    if resp == gabarito_5:
                        total_pontos += 1
                elif c == 6:
                    if resp == gabarito_6:
                        total_pontos += 1
                elif c == 7:
                    if resp == gabarito_7:
                        total_pontos += 1
                elif c == 8:
                    if resp == gabarito_8:
                        total_pontos += 1
                elif c == 9:
                    if resp == gabarito_9:
                        total_pontos += 1
                else:
                    if resp == gabarito_10:
                        total_pontos += 1
                break

    total_de_alunos += 1
    soma_pontos += total_pontos

    if total_de_alunos == 1:
        aluno_maior_nota = aluno
        maior_nota = total_pontos

        aluno_menor_nota = aluno
        menor_nota = total_pontos

    if total_pontos > maior_nota:
        aluno_maior_nota = aluno
        maior_nota = total_pontos

    if total_pontos < menor_nota:
        aluno_menor_nota = aluno
        menor_nota = total_pontos

    print('-'*30)

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('\033[93mAVISO: Informe uma resposta válida.\033[m')

    if continuar == 'N':
        break

media_pontos = soma_pontos / total_de_alunos

print('\033[96mFinalizando avaliação', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(1)
print('\033[m')

print('-'*50)
print(f'''\033[97ma) Maior e menor acerto:\033[m
\033[92m→ A maior nota foi de {aluno_maior_nota} com nota {maior_nota}
→ A menor nota foi de {aluno_menor_nota} com nota {menor_nota}

\033[97mb) Total de alunos que utilizaram o sistema:\033[m
\033[92m→ {total_de_alunos} alunos realizaram a avaliação

\033[97mc) A média das notas da turma:\033[m
\033[92m→ {media_pontos:.1f} pontos''')
