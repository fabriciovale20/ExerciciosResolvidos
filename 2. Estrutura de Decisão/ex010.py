"""
    Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

turno = input('Qual turno você estuda? ')

if turno in 'Mm':
    print('Bom dia!')
elif turno in 'Vv':
    print('Boa tarde!')
elif turno in 'Nn':
    print('Boa noite!')
else:
    print('Valor inválido!')
