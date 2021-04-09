turno = input('Qual turno você estuda? ')

if turno in 'Mm':
    print('Bom dia!')
elif turno in 'Vv':
    print('Boa tarde!')
elif turno in 'Nn':
    print('Boa noite!')
else:
    print('Valor inválido!')