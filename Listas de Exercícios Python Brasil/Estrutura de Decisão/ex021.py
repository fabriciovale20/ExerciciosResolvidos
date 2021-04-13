saque = int(input('Qual valor dos saque? R$'))

valores = {0:'', 1:'uma', 2:'duas', 3:'três', 4:'quatro', 5:'cinco', 6:'seis', 7:'sete', 8:'oito', 9:'nove', 10:'dez'}
nota_100 = nota_50 = nota_10 = nota_5 = nota_1 = 0
print(f'Para sacar a quantia de {saque} reais, o programa fornece ', end='')

while True:
    if saque >= 100:
        while saque >= 100:
            nota_100 += 1
            saque -= 100
        if nota_100 > 1:
            print(f'{valores[nota_100]} notas de 100, ', end='')
        else:
            print(f'{valores[nota_100]} nota de 100, ', end='')
    elif saque >= 50:
        while saque >= 50:
            nota_50 += 1
            saque -= 50
        if nota_50 > 1:
            print(f'{valores[nota_50]} notas de 50, ', end='')
        else:
            print(f'{valores[nota_50]} nota de 50, ', end='')
    elif saque >= 10:
        while saque >= 10:
            nota_10 += 1
            saque -= 10
        if nota_10 > 1:
            print(f'{valores[nota_10]} notas de 10, ', end='')
        else:
            print(f'{valores[nota_10]} nota de 10, ', end='')
    elif saque >= 5:
        while saque >= 5:
            nota_5 += 1
            saque -= 5
        if nota_5 > 1:
            print(f'{valores[nota_5]} notas de 5, ', end='')
        else:
            print(f'{valores[nota_5]} nota de 5, ', end='')
    elif 0 < saque < 5:
        while 0 < saque < 5:
            nota_1 += 1
            saque -= 1
        if nota_1 > 1:
            print(f'{valores[nota_1]} notas de 1. ', end='')
        else:
            print(f'{valores[nota_1]} nota de 1. ', end='')