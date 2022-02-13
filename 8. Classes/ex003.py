"""
    Exercício 3

    Classe Retangulo: Crie uma classe que modele um retangulo:

a) Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b) Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c) Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_valores(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def mostrar_valor(self):
        print(f'Base {self.base} | Altura {self.altura}')

    def calcular_area(self):
        print(f'Área igual a {self.base * self.altura} metros')

    def calcular_perimetro(self):
        print(f'Perímetro igual a {2*(self.base * self.altura)} metros')

    def piso_rodape(self):
        print(f'Precisará de {2*(self.base * self.altura)} metros de rodapé e {self.base * self.altura} unidades de piso.')

print('Informe os valores das medidas abaixo.')
base = int(input('Base: '))
altura = int(input('Altura: '))

retangulo = Retangulo(base, altura)
retangulo.mostrar_valor()
retangulo.calcular_area()
retangulo.calcular_perimetro()
print()

resp = input('Deseja modificar as medidas? [S/N] ').strip().lower()
if resp == 's':
    base = int(input('Base: '))
    altura = int(input('Altura: '))
    retangulo.mudar_valores(base, altura)
    print('Medidas atualizadas.')

    print()
    retangulo.mostrar_valor()
    retangulo.calcular_area()
    retangulo.calcular_perimetro()
    retangulo.piso_rodape()


