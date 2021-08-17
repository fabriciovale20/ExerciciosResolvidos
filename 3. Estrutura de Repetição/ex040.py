"""
    Exercício 40

    Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
a) Código da cidade;
b) Número de veículos de passeio (em 1999);
c) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:
d) Qual a maior e menor índice de acidentes de trânsito e que cidade pertence;
e) Qual a média de veículos nas cinco cidades juntas;
f) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""

from time import sleep

cidade_maior_acidente = cidade_menor_acidente = ''
maior_acidente = menor_acidente = media_veiculos = numero_cidades_menos_2000 = numero_acidentes_menos_2000 = 0

for c in range(1, 6):
    print('-'*13)
    print(f'  \033[97m{c}º COLETA\033[m')
    print('-' * 13)
    cidade = str(input('Código da cidade: '))
    numero_veiculo = int(input('Número de veículos de passeio: '))
    numero_acidentes_com_vitimas = int(input('Número de acidentes de trânsito com vítimas: '))

    # LETRA C
    if c == 1:
        cidade_maior_acidente = cidade_menor_acidente = cidade
        maior_acidente = menor_acidente = numero_acidentes_com_vitimas

    elif numero_acidentes_com_vitimas > maior_acidente:
        cidade_maior_acidente = cidade
        maior_acidente = numero_acidentes_com_vitimas

    elif numero_acidentes_com_vitimas < menor_acidente:
        cidade_menor_acidente = cidade
        menor_acidente = numero_acidentes_com_vitimas

    # LETRA E
    media_veiculos += numero_veiculo

    # LETRA F
    if numero_veiculo < 2000:
        numero_cidades_menos_2000 += 1
        numero_acidentes_menos_2000 += numero_acidentes_com_vitimas

    print('\033[96mRegistrando informações', end='')
    for i in range(0, 3):
        sleep(0.5)
        print('.', end='')
    print(' registrado.\033[m')


print('\033[97m\nInformações coletadas com sucesso.\nAguarde enquanto processamos os dados', end='')
for c in range(0, 3):
    sleep(0.5)
    print('.', end='')
print('\033[m\n')

print(f'''\033[97md)\033[m \033[93mQual a maior e menor índice de acidentes de trânsito e que cidade pertence;\033[m
→ Maior - Cidade: {cidade_maior_acidente} com {maior_acidente} acidentes
→ Menor - Cidade: {cidade_menor_acidente} com {menor_acidente} acidentes

\033[97me)\033[m \033[93mQual a média de veículos nas cinco cidades juntas;\033[m
→ Média de {media_veiculos / 5:.2f} veículos

\033[97mf)\033[m \033[93mQual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.\033[m
→ Média de {numero_acidentes_menos_2000 / numero_cidades_menos_2000:.2f} acidentes''')
