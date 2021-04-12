valor = int(input('Número menos que 1000: '))

if valor >= 1000:
    print('Valor informado inválido!')
else:
    valor = str(valor)
    if len(valor) == 3:
        if int(valor[0]) > 1:
            print(f'{valor[0]} centenas, ',end='')
        else:
            print(f'{valor[0]} centena, ',end='')
        if int(valor[1]) > 1:
            print(f'{valor[1]} dezenas e ', end='')
        else:
            print(f'{valor[1]} dezena e ', end='')
        if int(valor[2]) > 1:
            print(f'{valor[2]} unidades.')
        else:
            print(f'{valor[2]} unidade.')
    elif len(valor) == 2:
        if int(valor[0]) > 1:
            print(f'{valor[0]} dezenas e ', end='')
        else:
            print(f'{valor[0]} dezena e ', end='')
        if int(valor[1]) > 1:
            print(f'{valor[1]} unidades.')
        else:
            print(f'{valor[1]} unidade.')
    elif len(valor) == 1:
        if int(valor[0]) > 1:
            print(f'{valor[0]} unidades.')
        else:
            print(f'{valor[0]} unidade.')