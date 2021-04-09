letra = input('Informe se é M ou F: ')

if letra in 'Ff':
    print('F - Feminino')
elif letra in 'Mm':
    print('M - Masculino')
else:
    print('Valor inválido')