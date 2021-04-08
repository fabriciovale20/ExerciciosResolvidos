#Conversor de moedas
n = float(input('Informe quanto você tem na carteira: '))
dólar = n/3.27
print(f'Com o \033[1:30mR${n}\033[m você pode comprar \033[1:34mU${dólar:.2f}\033[m.')