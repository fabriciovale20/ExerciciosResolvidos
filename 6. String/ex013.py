"""
    Exercício 13

    Jogo da palavra embaralhada.
Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas.
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador terá seis tentativas para adivinhar a palavra.
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
"""

from random import randint

n = randint(0, 10) # Sorteando um número para escolher a linha correspondente a palavra do arquivo

with open(r'6. String/ex013_palavras.txt', 'r') as arquivo: # Abrindo arquivo de texto onde contém as palavras
    palavra = arquivo.readlines() # Lendo todas a palavras 

palavra_sorteada = list(palavra[n]) # Inserindo palavra sorteada na variável
del(palavra_sorteada[-1]) # Excluir o último elemento da lista que seria o "\n"
palavra_embaralhada = palavra_sorteada[::] # Inserindo palavra sorteada na variável para embaralhar
erros = 0
num = []

for c in palavra_sorteada:
    while True:
        indice = randint(0, len(palavra_sorteada)-1) # Escolhendo um número de acordo com o tamanho da string

        if indice in num: # Verificar se o índice sorteado já foi sorteado
            continue
        else:
            num.append(indice) # Adicionando o número sorteado a lista para não se repetir
            palavra_embaralhada[indice] = c # Adicionado a letra ao índice sorteado
            break # Para retornar para próxima letra da palavra

palavra_sorteada = ''.join(palavra_sorteada) # Transformando lista para string
palavra_embaralhada = ''.join(palavra_embaralhada) # Transformando lista para string
print(f'Palavra embaralhada: {palavra_embaralhada}')

while True:
    resp = input('Qual a palavra? ')

    if resp == palavra_sorteada: # Verificar se a palavra inserida pelo usuário corresponde a palavra sorteada
        print('PARABÉNS, VOCÊ ACERTOU!!!')
        break
    elif erros < 6: # Verificar o limite de tentativas
        erros += 1
        
        if erros == 6: # Se o usuário errar 6 vezes o programa é finalizado
            print('QUE PENA, SUAS CHANCES ACABARAM, VOCÊ PERDEU!!!')
            break
        else: # Se ainda estiver chances é exibido mensagem
            print(f'Você errou pela {erros}ª vez, você ainda tem {6 - erros} chances.')
