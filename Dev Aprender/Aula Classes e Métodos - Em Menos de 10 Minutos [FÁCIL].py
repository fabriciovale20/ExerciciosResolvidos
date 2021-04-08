from time import sleep

class Carro:
    def __init__(self, nome, marca, ano):
        self.nome = nome
        self.marca = marca
        self.ano = ano
    pass

    def ligar(self):
        print('Ligando o carro', end='')
        for n in range(0,3):
            sleep(0.8)
            print('.',end='')
        print('')
        print('Ligado!')

    def desligar(self):
        sleep(1)
        print('Desligando o carro',end='')
        for n in range(0,3):
            sleep(0.8)
            print('.',end='')
        print('')
        print('Desligado!')

    def informacoes(self):
        print(self.nome, self.marca, self.ano)

carro1 = Carro('Argo', 'Hyundai', '2019')
carro1.ligar()
carro1.desligar()
carro1.informacoes()
