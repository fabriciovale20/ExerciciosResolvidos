"""
    Exercício 8

    Classe Macaco:
    Desenvolva uma classe Macaco que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes
e verificando o conteúdo do estomago a cada refeição.

Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""

# Criado padrão Bucho de 1 à 2 (Faminto), de 3 à 6 (Satisfeito) e 7 até 10 (Cheio)

alimento_digerido = []

class Macaco():
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho

    def comer(self): # Função de adicionar comida ao bucho do macaco
        if self.bucho < 10:
            self.bucho += 1

    def verBucho(self): # Verificar status do bucho do macaco
        if self.bucho < 3:
            bucho_status = 'Faminto'
        elif 7 > self.bucho > 2:
            bucho_status = 'Satisfeito'
        else:
            bucho_status = 'Cheio'
        
        print(f'{self.nome} está {bucho_status}.')

        if len(alimento_digerido) > 0:
            print(f'Alimentos que ele você deu a eles:')
            for c in alimento_digerido:
                print(f'- {c}')
            

    def digerir(self, alimento):
        if self.bucho < 10 and alimento != 'Nada':
            alimento_digerido.append(alimento)
        self.comer()


print('Informações de cadastro dos Macacos')
print('MACACO 1')
nome_1 = input('Nome: ')
bucho_1 = int(input('Fome (1 à 10): '))
macaco_1 = Macaco(nome_1, bucho_1)

print('MACACO 2')
nome_2 = input('Nome: ')
bucho_2 = int(input('Fome (1 à 10): '))
macaco_2 = Macaco(nome_2, bucho_2)

while True:
    macaco_1.verBucho()
    comida_1 = input(f'Qual comida você vai dar ao Macaco {macaco_1.nome}? ').title().strip()

    macaco_2.verBucho()
    comida_2 = input(f'Qual comida você vai dar ao Macaco {macaco_2.nome}? ').title().strip()

    if comida_1 == 'Nada' and comida_2 == 'Nada':
        break

    macaco_1.digerir(comida_1)
    macaco_2.digerir(comida_2)
