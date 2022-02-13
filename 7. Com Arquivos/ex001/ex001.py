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
        ip_invalidos.append('.'.join(validar)) # IP inválido
    else:
        ip_validos.append('.'.join(validar)) # IP válido

print(ip_validos)
print(ip_invalidos)
ip_validos = '\n'.join(ip_validos)
ip_invalidos ='\n'.join(ip_invalidos)
print(ip_validos)
print(ip_invalidos)

with open(r'7. Com Arquivos/ex001/ip_validos.txt', 'w', encoding='utf8') as arquivo_valido:
    arquivo_valido.write('[Endereços válidos:]\n')
    arquivo_valido.write(ip_validos)

with open(r'7. Com Arquivos/ex001/ip_invalidos.txt', 'w', encoding='utf8') as arquivo_invalido:
    arquivo_invalido.write('[Endereços inválidos:]\n')
    arquivo_invalido.write(ip_invalidos)