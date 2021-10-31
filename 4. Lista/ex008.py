"""
    Exercício 8

    Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

# Existem dois tipos para declarar uma lista, como mostra o exemplo abaixo:
vetor_idade = list()
vetor_altura = []

for pessoa in range(1, 6):
    print(f'{pessoa}º pessoa')
    vetor_idade.append(int(input('Idade: ')))
    vetor_altura.append(float(input('Altura: ')))

print('-'*20)
print('Dados informados'.center(20))
print('-'*20)

for dados in range(len(vetor_idade)-1, -1, -1):
    print(f'{vetor_idade[dados]}, {vetor_altura[dados]}')
