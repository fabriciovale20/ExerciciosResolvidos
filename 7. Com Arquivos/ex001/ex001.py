"""
    Exercício 1

    Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
contendo um relatório dos endereços IP válidos e inválidos.

O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""

with open(r'7. Com Arquivos/ex001/ip.txt', 'r') as arquivo:
    ip = arquivo.readlines()

ip_validos = []
ip_invalidos = []

for c in ip:
    validar = c.split('.') # Dividir cada IP em uma lista
    validar[3] = validar[3].replace('\n','') # Retirar os '\n' da lista
    
    invalido = 0

    for n in validar:
        if int(n) > 255 or int(n) < 0: # Identificar se o IP é válido
            invalido += 1
        
    if invalido > 0:
        ip_invalidos.append('.'.join(validar)) # Adicionado a lista IP inválido
    else:
        ip_validos.append('.'.join(validar)) # Adicionado a lista IP válido

ip_validos = '\n'.join(ip_validos) # Transformar lista para string para poder ser registrado no arquivo TXT
ip_invalidos ='\n'.join(ip_invalidos) # Transformar lista para string para poder ser registrado no arquivo TXT

with open(r'7. Com Arquivos/ex001/ip_validos.txt', 'w', encoding='utf8') as arquivo_valido: # Arquivo de IP Válidos
    arquivo_valido.write('[Endereços válidos:]\n') # Escrevendo cabeçalho
    arquivo_valido.write(ip_validos) # Registrando no arquivo TXT os IP válidos

with open(r'7. Com Arquivos/ex001/ip_invalidos.txt', 'w', encoding='utf8') as arquivo_invalido: # Arquivo de IP Inválidos
    arquivo_invalido.write('[Endereços inválidos:]\n') # Escrevendo cabeçalho
    arquivo_invalido.write(ip_invalidos) # Registrando no arquivo TXT os IP inválidos