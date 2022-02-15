"""
    Exercício 4

    Classe Pessoa: Crie uma classe que modele uma pessoa:

a) Atributos: nome, idade, peso e altura
b) Métodos: Envelhercer, engordar, emagrecer, crescer.

Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhercer(self, anos): # Função envelhecer
        cont = 0

        while self.idade < 21 and cont <= anos: # Verificar se a idade é menor que 21 e adicionar os anos informados
            self.idade += 1
            self.altura += 0.05
            cont += 1
            anos -= 1 # A cada repetição é subtraído 1 ano para caso a idade utrapasse 21, o que sobrar será adicionado a idade na condição abaixo
        else:
            self.idade += anos # Adicionado os anos caso a idade seja maior que 21

    def engordar(self, ganhar_peso): # Função engordar
        self.peso += ganhar_peso

    def emagrecer(self, perder_peso): # Função emagrecer
        self.peso -= perder_peso

    def crescer(self, cresceu): # Função crescer
        self.altura += cresceu

    def mostrar_dados(self): # Função extra apenas para mostrar os dados no terminal para facilitar o acompanhamento
        print(f'''Nome: {self.nome}
Idade: {self.idade}
Peso: {self.peso} Kg
Altura: {self.altura} m''')
        print('-'*20)

pessoa = Pessoa('Fabrício', 18, 74.5, 1.67)
pessoa.mostrar_dados()

pessoa.envelhercer(5)
pessoa.engordar(1.5)
pessoa.emagrecer(1)
pessoa.crescer(0.3)

pessoa.mostrar_dados()
