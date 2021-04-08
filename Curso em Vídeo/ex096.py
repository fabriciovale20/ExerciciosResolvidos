print('Controle de Terrenos')
print('-'*(3+(len('Controle de Terrenos'))))

l = float(input('Largura m²: '))
c = float(input('Comprimento m²: '))

def área(l,c):
    a = l*c
    print(f'\nA área do Retângulo é de \033[1:30m{a:.2f}m²\033[m')

área(l,c)
