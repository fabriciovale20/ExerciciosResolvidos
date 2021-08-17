"""
    Exercício 3

    Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido.
"""

letra = input('Informe se é M ou F: ')

if letra in 'Ff':
    print('F - Feminino')
elif letra in 'Mm':
    print('M - Masculino')
else:
    print('Valor inválido')
