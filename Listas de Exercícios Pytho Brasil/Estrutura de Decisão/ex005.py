nota1= float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1+nota2)/2

print(f'Média : {media}')
if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')