#Sorteando um item na lista
import random
a1 = str(input('Primeiro aluno(a): '))
a2 = str(input('Segundo aluno(a): '))
a3 = str(input('Terceiro aluno(a): '))
a4 = str(input('Quarto aluno(a): '))
lista = [a1,a2,a3,a4]
c = random.choice(lista)
print(f'O alnuo(a) escolhido(a) foi \033[1:30m{c}\033[m.')
