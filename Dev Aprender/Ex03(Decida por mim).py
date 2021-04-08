import random
print('{:-^60}'.format(('JOGO DO FALA QUE EU TE RESPONDO')))
resp = ('Não sei, você quem sabe.','Rapaz, depende.','Dá certo sim.','Não, pelo amor de Deus','Vá perguntar isso a Coelho.')
pc = random.choice(resp)
n = str(input('Vamos começar? [S/N] ')).strip().upper()[0]
while n not in 'Nn':
    frase = str(input('Digite sua pergunta: '))
    pc = random.choice(resp)
    print(pc)
    n = str(input('Continuar? [S/N] ')).strip().upper()[0]
print('Valew Legal!')
