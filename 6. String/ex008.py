"""
    Exercício 8

    Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice-versa.
Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
Faça um programa que leia uma seqüência de caracteres, mostre-a e diga se é um palíndromo ou não.
"""

palavra = input('Digite a palavra: ').strip().upper().replace(" ","").replace("-","")

palavra_inversa = palavra[::-1] # Salvando em uma variável a string inversa

if palavra == palavra_inversa: # Testar se é políndromo
    polindromo = 'é'
else:
    polindromo = 'não é'

print(f'A palavra digitada {polindromo} um políndromo.')