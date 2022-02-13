"""
    Exercício 2

    A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários
com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório,
chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar
a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada,
que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada
pelo programa principal.
"""

def byte_to_mb(byte):
    mb = round(byte/1048576, 2) # Transformar de Byte para MB com arredondamento de 2 casa decimais

    return mb

def percentual_usado(mb):
    percentual = round(((mb*100)/total_ocupado), 2) # Calcular o percentual de cada espaço em relação ao total ocupado

    return percentual

total_ocupado = espaco_medio = porcentagem_uso = cont = 0
lista_usuarios = [] # Lista para salvar os dados dos usuários

with open(r'7. Com Arquivos/ex002/usuarios.txt', 'r') as usuarios:
    dados = usuarios.readlines() # Leitura dos registros do arquivo de usuarios.txt

for c in dados:
    usuario = str(c[0:16]).strip() # Salvar nome do usuário
    espaco_usuario = byte_to_mb(int(c[16:])) # Chamada da função para conversão de Byte para MB

    lista_usuarios.append([usuario, espaco_usuario]) # Adicionando o nome do usuário e o espaço utilzado a lista

    total_ocupado += espaco_usuario # Somar o espaço de cada usuário ao total

    cont += 1 # Contador para saber quanto usuários foram registrados e realizar a média

espaco_medio = round(total_ocupado / cont, 2) # Espaço médio do total e quantidade de usuários

with open(r'7. Com Arquivos/ex002/relatorios.txt', 'w', encoding='utf8') as registro: # Arquivo de saída com os registros
    registro.write(f'''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
''')
    
    cont = 1

    for c in lista_usuarios: # Condição utilizada para percorrer a lista de registros e salvar no arquivo relatorios.txt
        registro.write(f'{cont:^4} {c[0]:<15} {c[1]:>10} MB {percentual_usado(c[1]):>12} %\n')

        cont += 1

    registro.write(f'''\nEspaço total ocupado: {total_ocupado} MB
Espaço médio ocupado: {espaco_medio} MB''')