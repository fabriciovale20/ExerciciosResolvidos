#Par ou Ímpar?
n = int(input('Me diga um número qualquer: '))
if n%2 == 0:
    print(f'O númerero {n} é \033[34mPAR\033[m.')
else:
    print(f'O número {n} é \033[31mÍMPAR\033[m.')