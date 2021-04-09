peso = int(input('Informe o peso pescado: '))
excesso = peso - 50
multa = excesso * 4
print(f'João pescou {peso} Kg, {excesso} Kg de excesso, totalizando uma multa de R${multa:.2f}')