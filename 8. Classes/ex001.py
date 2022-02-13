"""
    Exercício 1

    Classe Bola: Crie uma classe que modele uma bola:

a) Atributos: Cor, circunferência, material
b) Métodos: trocaCor e mostraCor    
"""

class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostrarCor(self):
        print(f'A cor da bola é {self.cor}')

# Exemplo
bola = Bola('branca', 50, 'borracha')
bola.mostrarCor()
bola.trocaCor('azul')
bola.mostrarCor()