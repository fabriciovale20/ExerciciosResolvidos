n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1+n2)/2

print('-'*40)
print(f'Primeira nota {n1}')
print(f'Segunda nota {n2}')
print(f'Média {media}')
print('-'*40)
if 10 >= media >= 9:
    print('Conceito A, aprovado.')
elif 9 > media >= 7.5:
    print('Conceito B, aprovado.')
elif 7.5 > media >= 6:
    print('Conceito C, aprovado.')
elif 6 > media >= 4:
    print('Conceito D, reprovado.')
elif media > 4:
    print('Conceito E, reprovado.')