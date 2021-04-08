#Jogo da adivinhação v.1.0
import random
print('\033[1:33m=-\033[m'*30)
print('Vou pensar de  um numéro entre 0 e 5. \033[1:34mTente adivinhar...\033[m')
print('\033[1:33m=-\033[m'*30)
n = int(input('Em que número eu pensei? '))
print('\033[1:35mPROCESSSANDO...\033[m')
pc = random.randint(0,5)
if n == pc:
    print('\033[33mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print(f'\033[31mGANHEI! Eu pensei no número {pc} e não no {n}.\033[m')