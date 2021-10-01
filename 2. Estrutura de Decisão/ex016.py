"""
    Exercício 16

    Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
os demais valores, sendo encerrado;
b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

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
