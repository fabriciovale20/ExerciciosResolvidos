"""
    Exercício 11

    Jogo de Forca.
    Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""

from random import randint

n = randint(0, 10)
erros = 0

with open('ex011_palavras.txt', 'r') as arquivo:
    palavra = arquivo.readlines()

palavra_sorteada = palavra[n].upper()
acertos = []

for _ in range(len(palavra_sorteada)-1):
    acertos.append('_')

print('Jogo da Foca')
while True:
    letra = input('Digite uma letra: ').upper()

    if letra in palavra_sorteada:
        for pos, valor in enumerate(palavra_sorteada):
            if letra == valor:
                acertos[pos] = letra
        
        for c in acertos:
            print(c, end=' ')
        print('')

        if '_' not in acertos:
            print('PARABÉNS, VOCÊ VENCEU!!!')
            break
    
    else:
        erros += 1
        if erros < 6:
            print(f'Você errou pela {erros}º vez. Tente novamente')
        else:
            print(f'Você errou pela {erros}º vez. VOCÊ PERDEU')
            break
