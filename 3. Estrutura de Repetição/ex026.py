numero_de_eleitores = int(input('Número de eleitores: '))

print(f'{numero_de_eleitores} eleitores iram votar.\n'
      f'Candidatos:\n'
      f'(1) Jair Bolsonaron\n'
      f'(2) Luíz Inácio\n'
      f'(3) Michel Temer\n'
      f'(0) \033[97mNULO\033[m')

canditato1 = canditato2 = canditato3 = nulo = 0

nome_candidato1 = 'Jair Bolsonaro'
nome_candidato2 = 'Luiz Inácio'
nome_candidato3 = 'Michel Temer'

for c in range(1, numero_de_eleitores+1):
    try:
        voto = int(input(f'{c}º voto: '))
    except ValueError:
        voto = int(input(f'Voto inválido, tente novamente {c}º eleitor: '))
    while voto > 3:
        voto = int(input(f'Voto inválido, tente novamente {c}º eleitor: '))
    if voto == 1:
        canditato1 += 1
    elif voto == 2:
        canditato2 += 1
    elif voto == 3:
        canditato3 += 1
    elif voto == 0:
        nulo += 1
if canditato1 != canditato2 != canditato3 != canditato1:
    if canditato1 > canditato2 and canditato1 > canditato3:
        primeiro = nome_candidato1
        if canditato2 > canditato3:
            segundo = nome_candidato2
            terceiro = nome_candidato3
        else:
            segundo = nome_candidato3
            terceiro = nome_candidato2
    elif canditato2 > canditato1 and canditato2 > canditato3:
        primeiro = nome_candidato2
        if canditato1 > canditato3:
            segundo = nome_candidato1
            terceiro = nome_candidato3
        else:
            segundo = nome_candidato3
            terceiro = nome_candidato1
    elif canditato3 > canditato1 and canditato3 > canditato2:
        primeiro = nome_candidato3
        if canditato1 > canditato2:
            segundo = nome_candidato1
            terceiro = nome_candidato2
        else:
            segundo = nome_candidato2
            terceiro = nome_candidato1

    print(f'Total de votos: {numero_de_eleitores}\n'
          f'Jair Bolsonaro: {canditato1}\n'
          f'Luiz Inácio: {canditato2}\n'
          f'Michel Temer: {canditato3}\n'
          f'Votos nulos: {nulo}\n')

    print(f'--- VENCEDOR {primeiro} ---\nSegundo lugar: {segundo}\nTerceiro lugar: {terceiro}')
else:
    if canditato1 == canditato2:
        empate = f'{nome_candidato1} e {nome_candidato2}'
    elif canditato1 == canditato3:
        empate = f'{nome_candidato1} e {nome_candidato3}'
    else:
        empate = f'{nome_candidato2} e {nome_candidato3}'
    print(f'--- EMPATE ---\n'
          f'Houve um empate entre {empate}.')
