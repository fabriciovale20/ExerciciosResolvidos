#Média aritmética
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
média = (n1+n2)/2
if média >= 7:
    print(f'A média das entre \033[30m{n1}\033[m e \033[30m{n2}\033[m foi \033[34m{média}\033[m.')
else:
    print(f'A média das entre \033[30m{n1}\033[m e \033[30m{n2}\033[m foi \033[31m{média}\033[m.')