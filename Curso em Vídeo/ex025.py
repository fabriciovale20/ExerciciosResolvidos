#Procurando uma string dentro de outra
nome = str(input('Qual o seu nome completo? ')).upper().strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))
