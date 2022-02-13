"""
    Exercício 12

    Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste
conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133    
"""

telefone = input('Telefone: ').strip().replace('-','')

for c in telefone:
    if c.isalpha():
        print('Telefone inválido, informe apenas números!')
        break
else:
    if len(telefone) < 7 or len(telefone) > 8:
        print('Telefone inválido, total de dígitos!')
    elif len(telefone) == 7:
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        telefone = '3' + telefone
        print(f'Telefone corrigido sem formatação: {telefone}')
        telefone = telefone[:4] + '-' + telefone[4:]
        print(f'Telefone corrigido com formatação: {telefone}')
