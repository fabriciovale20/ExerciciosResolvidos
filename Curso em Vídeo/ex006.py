#Dobro, triplo e raiz quadrada
import math
n = int(input('Informe um número: '))
dobro = n*2
triplo = n*3
raiz = math.sqrt(n)
print('=-'*20)
print(f'\033[30mVocê escolhe o número: {n}\033[m')
print(f'Dobro: {dobro}')
print(f'Triplo: {triplo}')
print(f'Raiz quadrada: {raiz}')