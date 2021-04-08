#Aluguel de Carros
print('-'*20)
print('ALUGUEL DE CARROS')
print('-'*20)
d = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
diária = 60*d
distância = 0.15*km
soma = diária+distância
print(f'O total à pagar é de \033[7:1:4:31mR${soma:.2f}\033[m.')