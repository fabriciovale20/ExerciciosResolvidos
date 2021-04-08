import random
print('{:-^40}'.format('SIMULADO DE DADOS'))
resp = str(input('Vamos começar? [S/N] ')).strip().upper()[0]
dado = 0
while resp not in 'Nn':
    dado = random.randint(1, 6)
    print(f'O número sorteado foi {dado}.')
    resp = str(input('Vamos jogar? [S/N] ')).strip().upper()[0]
print('{:-^40}'.format('PROGRAMA FINALIZADO'))