a = int(input('Valor de A: '))
if a > 0:
    b = int(input('Valor de B: '))
    c = int(input('Valor de C: '))
    print('-'*30)
    print('{:^30}'.format('Equação de Segundo Grau'))
    print('-'*30)
    print(f'Equação {a}x² + {b}x + {c} = 0')
    delta = (b**2)-(4*a*c)
    if delta == 0:
        print('A equação possui apenas UM raiz.')
    elif delta > 0:
        print('A equação possui DUAS raizes.')
    elif delta < 0:
        print('A equação NÃO possui raizes reais.')
else:
    print('Valor de A igual a zero, encerrando programa.')