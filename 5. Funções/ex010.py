"""
    Exercício 10

    Jogo de Craps.
    Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada,
isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""

from random import randint
from time import sleep

def jogar():
    num = randint(2, 12)

    return num

ganhar = [7, 11]
perder = [2, 3, 12]
jogadas = 0

while True:
    resp = input('Jogar dados [S/N]? ')
    num = jogar() # Jogando os dados

    jogadas += 1

    print('Jogando os dados', end='')
    for c in range(3):
        sleep(0.5)
        print('.', end='')
    print(f'  \033[97m{num}\033[m') # Número sorteado nos dados

    if jogadas == 1:
        if num in ganhar:
            print(f'Você ganhou!!!') # Caso for a primeira jogada e tirar os números da lista "ganhar"
            break
        elif num in perder:
            print(f'Você perdeu!!!') # Caso for a primeira jogada e tirar os números da lista "perder"
            break
        else:
            num_para_ganhar = num # Número que será necessário repetir para o jogar ganhar
            print(f'Para ganhar, você precisa tirar {num_para_ganhar} de novo, se tirar 7, você perde.')
    
    if jogadas > 1:
        if num == num_para_ganhar:
            print(f'Você conseguiu, parabéns!!!') # Se o resultado da jogar for o mesmo número reservado
            break
        elif num == 7:
            print(f'Você tirou {num} e perdeu!!!') # Se o jogar tirar o número 7
            break
