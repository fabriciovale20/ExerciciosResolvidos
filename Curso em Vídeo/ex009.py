#Tabuada
print('-'*30)
print('-----\033[1:30mPROGRAMA DE TABUADA\033[m------')
print('-'*30)
n = int(input('Digíte um número: '))
cont = mult = 0
for cont in range(1,11):
    mult = n*cont
    print(f'{n} x {cont} = {mult}')
print('='*20)