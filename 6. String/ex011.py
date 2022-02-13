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

n = randint(0, 10) # Número sorteado que corresponde a linha do arquivo de texto
erros = 0

with open(r'6. String/ex011_palavras.txt', 'r') as arquivo: # Abrir o arquivo de texto que contém as palavras
    palavra = arquivo.readlines()

palavra_sorteada = palavra[n].upper() # Salvando na variável a palavra sorteada
acertos = [] # Lista onde ficará os acertos das letras

for _ in range(len(palavra_sorteada)-1): # Montar a lista com os espaços
    acertos.append('_')

print('Jogo da Foca')
while True:
    letra = input('Digite uma letra: ').upper()

    if letra in palavra_sorteada: # Condição para inserir a letra escolhida dentro da lista de ACERTOS caso a letra escolhida for certa
        for pos, valor in enumerate(palavra_sorteada):
            if letra == valor:
                acertos[pos] = letra # Irá salvar a letra no índice correspondente
        
        for c in acertos: # Mostrar a lista na tela para informar ao usuário o que falta
            print(c, end=' ')
        print('')

        if '_' not in acertos: # Caso não haja mais espaço para preencher o usuário vence
            print('PARABÉNS, VOCÊ VENCEU!!!')
            break
    
    else:
        erros += 1
        if erros < 6: # Se o usuário errar 6 vezes o programa e finalizado
            print(f'Você errou pela {erros}º vez. Tente novamente')
        else:
            print(f'Você errou pela {erros}º vez. VOCÊ PERDEU')
            break
