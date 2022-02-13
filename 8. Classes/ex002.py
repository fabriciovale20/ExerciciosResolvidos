"""
    Exercício 2

    Classe Quadrado: Crie uma classe que modele um quadrado:

a) Atributos: Tamanho do lado
b) Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado():
    def __init__(self, tam_lado):
        self.tam_lado = tam_lado
    
    def mudarLado(self, novo_lado):
        self.tam_lado = novo_lado

    def valor_lado(self):
        print(f'O lado é {self.tam_lado}')

    def calcular_area(self):
        print(f'Área é igual a {self.tam_lado**2}') # Área do quadrado é Lado x Lado ou Lado²

# Exemplo
quadrado = Quadrado(3)
quadrado.mudarLado(4)
quadrado.valor_lado()
quadrado.calcular_area()
