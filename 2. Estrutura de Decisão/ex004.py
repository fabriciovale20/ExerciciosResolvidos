"""
    Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input('Digite uma letra: ')

print('Letra digitada ',end='')
if letra in 'AaEeIiOoUu':
    print('é uma vogal.')
else:
    print('não é uma vogal.')
