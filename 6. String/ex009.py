"""
    Exercício 9

    Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.
"""

cpf = input('Inform seu CPF (xxx.xxx.xxx-xx): ')
letra = 0

if len(cpf) != 14 or cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
    print('\033[1;91mCPF formato inválido!\033[m')
else:
    for c in cpf:
        if c.isalpha():
            letra += 1

    if letra == 0:
        print('\033[1;32mCPF válido!!!\033[m')
    else:
        print('\033[1;91mCPF inválido possui letras!\033[m')
