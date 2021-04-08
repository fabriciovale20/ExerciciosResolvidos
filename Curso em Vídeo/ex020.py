#Sorteando uma ordem na lista
import random
a1 = str(input('Primeiro aluno(a): '))
a2 = str(input('Segundo aluno(a): '))
a3 = str(input('Terceiro aluno(a): '))
a4 = str(input('Quarto aluno(a): '))
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('-'*20)
print('A ordem de apresentação será:')
print(f'\033[1:30m→ Primero: {lista[0]}\033[m\n\033[3:30m→ Segundo: {lista[1]}\033[m'
      f'\n\033[1:30m→ Terceiro: {lista[2]}\033[m\n\033[3:30m→ Quarto: {lista[3]}\033[m')

