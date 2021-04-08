#Seno, cosseno e tangente
import math
n = float(input('Digite o valor: '))
print(f'O ângulo de \033[30m{n}\033[m tem:')
print(f'SENO = {math.sin(math.radians(n)):.2f}')
print(f'COSSENO = {math.cos(math.radians(n)):.2f}')
print(f'TANGENTE = {math.tan(math.radians(n)):.2f}')
